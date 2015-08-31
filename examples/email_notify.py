import pylogging
import os

# Logs Dir Absolute Path
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
# Create Logger Instance
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path)
# Activate email alerting
logger.setConfig('ALERT_STATUS', True)
# Set default message subject
logger.setConfig('ALERT_SUBJECT', "My APP Alert")
# Email to send message to
logger.setConfig('ALERT_EMAIL', 'you@gmail.com')
# OR send message to many emails
logger.setConfig('ALERT_EMAIL', 'you@gmail.com,alex@gmail.com,mary@gmail.com')
# Message types to receive alerts for
logger.setConfig('ALERT_TYPES', ['critical', 'error'])

# our own SMTP server (Library uses gmail)
logger.setConfig('MAILER_HOST', 'smtp.gmail.com')
# SMTP server port
logger.setConfig('MAILER_PORT', 587)
# SMTP server username (your gmail email)
logger.setConfig('MAILER_USER', 'you@gmail.com')
# SMTP server password (your gmail password)
logger.setConfig('MAILER_PWD', 'gmailpass')

# Message from
logger.setConfig('MAILER_FROM', 'you@gmail.com')


# Log Info Message
logger.info("Info Message")
# Log Normal Message
logger.log("Normal Log Message.")
# Log Warning Message
logger.warning("Warning Message.")
# Log Error Message (with email notification)
logger.error("Error Message.")
# Log Critical Message (with email notification)
logger.critical("Critical Message.")