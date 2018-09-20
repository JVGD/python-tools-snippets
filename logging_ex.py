import logging
from logging.handlers import RotatingFileHandler

# Handler conf
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = RotatingFileHandler('carrier_watchdog.log', maxBytes=2000, backupCount=10)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

# You can define different names for different
# loggers within the app, ideally you can call
# a logger per file with name __file__ and then
# use logger at every place
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

if __name__ == "__main__":

	try:
		for n in range(200):
			logger.debug(str(n) + ' debug message')
			logger.info(str(n) + ' info message')
			logger.warn(str(n) + ' warn message')
			logger.error(str(n) + ' error message')
			logger.critical(str(n) + ' critical message')
			if n == 100:
				raise IOError("This is an error")
	
	except Exception as e:
		# Log and dumps error info
		logger.error('Exception caught', exc_info=True)
		# Raise exception again
		raise e