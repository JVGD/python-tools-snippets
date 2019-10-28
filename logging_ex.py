import logging
import sys
import time
from logging.handlers import RotatingFileHandler

def get_logger(name=None, level=None, log_file=None):

    # Parsing args
    if not name:
        name = __name__

    log_levels = [logging.CRITICAL, logging.FATAL,
                  logging.ERROR, logging.WARNING, 
                  logging.INFO, logging.DEBUG, 
                  logging.NOTSET]

    if level not in log_levels:
       level = logging.INFO

	# Configuring root logger
    log_format = '%(asctime)s %(name)s [%(levelname)s] %(message)s'
    logging.basicConfig(
        level=logging.CRITICAL, 
        format=log_format)

    # Getting child logger with setted name and level
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Handler for logging to a file if log_file is set
    if log_file:
        file_handler = RotatingFileHandler(
            filename=log_file, 
            maxBytes=2000, 
            backupCount=10)
        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)

        # Adding hanlders to child logger only
        # if there is not any other handler already
        if len(logger.handlers) == 0:
            logger.addHandler(file_handler)

    # Returning child logger
    return logger


if __name__ == "__main__":
	log = get_logger(__name__, level=logging.INFO, log_file='app.log')

	for i in range(10):
		log.info('Iteration %s', i)
		log.warning('Iteration %s', i)
		time.sleep(2)

	log.info('Finished')