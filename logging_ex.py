import logging
import sys
from logging.handlers import RotatingFileHandler

# General formater for logs in here we define the logs format
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')

# Handler for logging to stdout
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# Handler for logging to a file
file_handler = RotatingFileHandler('carrier_watchdog.log', maxBytes=2000, backupCount=10)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Getting the logger that will handle multiple handlers
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.propagate = False


if __name__ == "__main__":

	try:
		for n in range(1000):
			logger.debug(str(n) + ' debug message')
			logger.info(str(n) + ' info message')
			logger.warn(str(n) + ' warn message')
			logger.error(str(n) + ' error message')
			logger.critical(str(n) + ' critical message')
			if n == 900:
				# Forcing an error
				raise IOError("This is a forced error")
	
	except Exception as e:
		# Log and dumps error info
		logger.error('Exception caught', exc_info=True)
		# Raise exception again
		raise e