import json_log_formatter
from logging import Formatter, LoggerAdapter, StreamHandler, getLogger, INFO, WARNING
from sys import stdout, stderr

def init_root_logger(level=WARNING):
    logger = getLogger(__name__.split('.')[0])
    logger.setLevel(level)
    
    formatter = json_log_formatter.VerboseJSONFormatter()
    
    info_handler = StreamHandler(stdout)
    info_handler.addFilter(lambda x: x.levelno <= INFO)
    info_handler.setFormatter(formatter)
    logger.addHandler(info_handler)

    error_handler = StreamHandler(stderr)
    error_handler.addFilter(lambda x: x.levelno > INFO)
    error_handler.setFormatter(formatter)
    logger.addHandler(error_handler)

    logger = LoggerAdapter(logger, {
        'task': 'root',
        'endpoint': False,
        'httpMethod': '',
        'httpPath': '',
    })
    
    return logger
