import logging
import sys
from logging import StreamHandler
from os import getenv

from flask import Flask

from endpoints.correlate import get_correlations
from endpoints.headers import log_header
from endpoints.hello import say_hello
from loggers.json_logging import init_json_logging
from loggers.loguru import init_loguru
from loggers.structlog import init_structlog

app = Flask(__name__)

# Configure the different logging option
logging_level = logging.INFO
logger = logging.getLogger("test_app")
structured_logging = getenv("FLASK_DEBUG", "").lower() not in ("1", "true", "yes", "y")
match getenv("LOG_FRAMEWORK"):
    case "json_logging":
        init_json_logging(app, logging_level, structured_logging)
    case "structlog":
        init_structlog(app, logging_level, structured_logging)
    case "loguru":
        init_loguru(app, logging_level, structured_logging)
    case _:
        logging.basicConfig(level=logging_level, handlers=[StreamHandler(sys.stdout)])


@app.route('/')
def hello_world():
    logger.info("route hello_world")
    return say_hello()


@app.route('/error')
def raise_error():
    raise ValueError("I have an exception")


@app.route('/correlate')
def correlate():
    logger.info("returning correlations")
    return get_correlations()


@app.route('/header/<header>')
def header_endpoint(header):
    logger.info("going to log a header")
    return log_header(header)


if __name__ == '__main__':
    app.run()
