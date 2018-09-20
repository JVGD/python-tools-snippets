import logging
import sys
from logging.handlers import RotatingFileHandler

# General formater for logs in here we define the logs format
formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s')

# Handler for logging to a file
file_handler = RotatingFileHandler('carrier_watchdog.log', maxBytes=2000, backupCount=10)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# Handler for logging to stdout
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# You can define different names for different
# loggers within the app, ideally you can call
# a logger per file with name __file__ and then
# use logger at every place, you can also have
# different handlers within one logger
logger = logging.getLogger(__file__)
# Set global level of logging
logger.setLevel(logging.DEBUG)
# Adding handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)


if __name__ == "__main__":

	try:
		for n in range(1000):
			logger.debug(str(n) + ' debug message')
			logger.info(str(n) + ' info message')
			logger.warn(str(n) + ' warn message')
			logger.error(str(n) + ' error message')
			logger.critical(str(n) + ' critical message')
			if n == 900:
				raise IOError("This is an error")
	
	except Exception as e:
		# Log and dumps error info
		logger.error('Exception caught', exc_info=True)
		# Raise exception again
		raise e