import pylogging
import os

# Logs Dir Absolute Path
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
# Create Logger Instance
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path)
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