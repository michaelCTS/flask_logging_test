

import logging
import sys

import structlog
from flask import Flask


def init_structlog(app: Flask, logging_level: int, structured: bool = True):
    structlog.configure(
        processors=[
            # Prepare event dict for `ProcessorFormatter`.
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
    )

    formatter = structlog.stdlib.ProcessorFormatter(
        processors=[
            structlog.processors.JSONRenderer()
            if structured else structlog.dev.ConsoleRenderer()
        ],
    )

    handler = logging.StreamHandler(sys.stdout)
    # Use OUR `ProcessorFormatter` to format all `logging` entries.
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    root_logger.setLevel(logging_level)
