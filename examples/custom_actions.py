import pylogging
import os

# Logs Dir Absolute Path
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
# Create Logger Instance
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path)

def customAction1(type, msg):
	# Custom Action Goes Here
	pass

# Add Action
actionIden1 = logger.addAction(customAction1)

def customAction2(type, msg):
	# Custom Action Goes Here
	pass

# Add Action
actionIden2 = logger.addAction(customAction2)

# To Remove Action1
logger.removeAction(actionIden1)


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