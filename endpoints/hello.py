
import logging

logger = logging.getLogger(__name__)


def say_hello():
    logger.info("about to say hello")
    return "Hello world!"
