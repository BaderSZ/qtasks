"""Service manager class. Contains the necessary functions to create and build api discovery \
    service."""

try:
    from os import path
    import logging

    # Auth libs
    from google.auth.transport.requests import Request
    from google.auth.exceptions import (OAuthError, ReauthFailError,
                                        RefreshError, TransportError)

    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    # API libs
    from googleapiclient.discovery import build
    from googleapiclient.discovery import Resource
    from googleapiclient.errors import HttpError

    # Local
    from qtasks.keys import keys
    from qtasks import config

    # Types
    from qtasks.gtypes.exceptions import AuthenticationError
    from qtasks.gtypes.skeleton import ServiceManagerType

except ImportError as importexp:
    logging.critical("Import Exception: Could not import a library!\n %s", importexp)
    raise


class ServiceManager(ServiceManagerType):
    """Google Services manager object. Creates and manages keys and services."""

    def __init__(self) -> None:
        """Initiate an empty object."""
        super().__init__()

    def create_key(self, token_file: str) -> None:
        """Create a client key given a token file."""
        # TODO: Other authentication methods
        try:
            flow = InstalledAppFlow.from_client_secrets_file(keys.CLIENT_SECRETS_FILE, config.SCOPES)
            self.credentials = flow.run_local_server()  # Opens local tab
        except ValueError as verr:
            logging.critical("flow could not create credentials! Check docs (and comment) %s", verr)
            raise
        with open(token_file, 'w') as token:
            token.write(self.credentials.to_json())

    def create(self, token_file: str) -> Resource:
        """Create a Resource for interacting with the Google Tasks API."""
        # Get token
        if path.exists(token_file):
            logging.info("Found token %s. Using...", token_file)
            try:
                self.credentials = Credentials.from_authorized_user_file(token_file, config.SCOPES)
                if not self.credentials or not self.credentials.valid:
                    if (self.credentials and self.credentials.expired and self.credentials.refresh_token):
                        logging.info("Refreshing expired token")
                        self.credentials.refresh(Request())
                    else:
                        self.create_key(token_file)
            except (OAuthError, ReauthFailError, RefreshError, TransportError) as authexp:
                logging.exception("Could not create credentials!\n%s", authexp)
                logging.exception("Try again?")
                raise AuthenticationError("Could not authenticate: ") from authexp
            except OSError as exp:
                logging.critical("Could not open file! %s", exp)
                raise
        else:
            logging.info("No token file found. Creating...")
            self.create_key(token_file)
        try:
            self.service = build(config.API_SERVICE_NAME, config.API_VERSION, credentials=self.credentials)
        except HttpError as httperr:
            logging.exception("Exception error: Request failed\n%s", httperr)
