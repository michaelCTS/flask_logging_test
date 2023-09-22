
import logging

from flask import request

logger = logging.getLogger(__name__)


def get_correlations():
    if correlation_id := request.headers.get("X-Correlation-ID"):
        logger.info(
            "Got a request with a correlation",
            extra={"correlation_id": correlation_id}
        )
        return correlation_id
    else:
        return "No correlation ID!", 400
