import logging

def setup_logger():
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.DEBUG)

    # File handler (detailed logs)
    fh = logging.FileHandler('trading_bot.log')
    fh.setLevel(logging.DEBUG)

    # Console handler (summary)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add handlers
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger

logger = setup_logger()
