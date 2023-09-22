
import inspect
import logging
import sys

from flask import Flask
from loguru import logger


def init_loguru(app: Flask, log_level: int, structured: bool = True):
    class InterceptHandler(logging.Handler):
        def emit(self, record: logging.LogRecord) -> None:
            # Get corresponding Loguru level if it exists.
            level: str | int
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = record.levelno

            # Find caller from where originated the logged message.
            frame, depth = inspect.currentframe(), 0
            while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
                frame = frame.f_back
                depth += 1

            props = getattr(record, "props", {})
            logger.opt(depth=depth, exception=record.exc_info).log(
                level,
                record.getMessage(),
                **props
            )

    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    logger.remove()
    logger.add(sys.stdout, serialize=structured, level=log_level)

    logger.info("Now logging with loguru")
