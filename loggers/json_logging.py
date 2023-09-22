
import logging
import sys
from logging import StreamHandler

import json_logging
from flask import Flask


def init_json_logging(app: Flask, level: int, structured: bool = True):
    logging.basicConfig(level=level, handlers=[StreamHandler(sys.stdout)])

    json_logging.init_flask(enable_json=structured)
    json_logging.init_request_instrument(app)

    # Ensure the json logging is applied everywhere
    json_logging.config_root_logger()
