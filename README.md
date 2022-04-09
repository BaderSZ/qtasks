# QTasks/GTasks

This is a work-in-progress. Documentation will come soon.

### A soon-to-be Google Tasks wrapper and Library

## Requirements
 - python
 - google-auth
 - google-auth-oauthlib
 - google-api-core
 - google-api-python-client
 - PySide6

The hardest dependency is python `>=3.10,<3.11` due to PySide6.

You will need to create your own project and corresponding client secrets file for now in the [google developer console](https://console.cloud.google.com/apis/credentials) with the scopes in [config.py](qtasks/manager/config.py).

## Building and running
```sh
poetry run generate-all  # Generate .py files for resources and UI
poetry install
```
To run:
```sh
poetry run generate-all 
poetry run main  # starts up the GUI
```

## Virtualenv

 - Created via [poetry](https://python-poetry.org/docs/cli/#env).
 - Python binary is (usually) in `.venv/bin/python`
 - You can enable with `source venv/bin/activate` and disable with `deactivate`

## License
See [the LICENSE.txt file](LICENSE.txt) for the GPL v3.0 text. 
