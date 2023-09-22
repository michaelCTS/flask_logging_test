
import logging

from flask import request

logger = logging.getLogger(__name__)


def log_header(header: str):
    if value := request.headers.get(header):
        logger.info("Got a header with a value", extra={"props": {"my_header": value}})
        return value
    return "Header has no value", 400
