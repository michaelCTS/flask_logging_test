# Flask structured logging tests

Run with `python -m flask run`

## Setting the logging framework

Use the `LOG_FRAMEWORK` env-var to on of
  - `json_logging`
  - `loguru`
  - `structlog`

## Debug mode

Enabling debug mode will turn off structured logging to improve developer experience.
It will thus log normally and you won't have to parse JSON while developing.
