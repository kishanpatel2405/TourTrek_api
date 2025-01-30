import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def log_info(message: str):
    logger.info(message)
