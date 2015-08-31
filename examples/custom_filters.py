import pylogging
import os

# Logs Dir Absolute Path
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
# Create Logger Instance
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path)

def customFilter1(type, msg):
	# Filter message text here
	return msg

# Add Filter
filterIden1 = logger.addFilter(customFilter1)

def customFilter2(type, msg):
	# Filter message text here
	return msg

# Add Filter
filterIden2 = logger.addFilter(customFilter2)

# To Remove Filter1
logger.removeFilter(filterIden1)


# Log Info Message
logger.info("Info Message")
# Log Warning Message
logger.warning("Warning Message.")
# Log Error Message
logger.error("Error Message.")
# Log Critical Message
logger.critical("Critical Message.")
# Log Normal Message
logger.log("Normal Log Message.")