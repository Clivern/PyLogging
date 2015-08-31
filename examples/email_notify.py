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
# Add your email
logger.setConfig('ALERT_EMAIL', 'hello@example.com')
# OR you can use this in case of multi emails
logger.setConfig('ALERT_EMAIL', 'hello@example.com,hello2@example.com,hello3@example.com')
# Message types to receive alerts for
logger.setConfig('ALERT_TYPES', ['critical', 'error'])

# our own SMTP server
logger.setConfig('MAILER_HOST', 'localhost')
# SMTP server username
logger.setConfig('MAILER_USER', None)
# SMTP server password
logger.setConfig('MAILER_PWD', None)

# Message from header value
logger.setConfig('MAILER_FROM', 'no_reply@example.com')