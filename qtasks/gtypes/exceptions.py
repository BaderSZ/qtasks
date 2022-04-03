"""Custom exceptions for QTasks module."""


class Error(Exception):
    """General error object. Fail instead of warn."""

    def __init__(self, message):
        """Call inherited Exception class init."""
        self.message = message
        super().__init__(self.message)


class AuthenticationError(Error):
    """Object for credentials/flow authentication errors."""

    def __init__(self, message):
        """Call inherited Exception class init."""
        self.message = message
        super().__init__(self.message)


class NoServiceAvailable(Exception):
    """Use when no (task or tasklist) service is available."""

    def __init__(self, message):
        """Call inherited Exception class init."""
        self.message = message
        super().__init__(self.message)


class DisabledAPIException(Exception):
    """Warn when the API (according to docs) is read-only or disabled."""

    def __init__(self, message):
        """Call inherited Exception class init."""
        self.message = message
        super().__init__(self.message)


class ExecutionError(Error):
    """Could not execute requests."""

    def __init__(self, message):
        """Call inherited Exception class init."""
        self.message = message
        super().__init__(self.message)
