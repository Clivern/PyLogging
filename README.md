PyLogging
=========

PyLogging is a light-weight python logging library. It provides ability to write logs in your own customized format. It is also provides support for custom log filters, custom log actions and email notifications.

*Current version: [v1.0.0]*

[![Build Status](https://travis-ci.org/Clivern/PyLogging.svg?branch=master)](https://travis-ci.org/Clivern/PyLogging)

Installation
------------
To install PyLogging run this command:
```
pip install pylogging
```
or [download](https://github.com/Clivern/pylogging/archive/1.0.0.zip) Package then run this command:
```
pip install PyLogging-1.0.0.zip
```

Usage
-----
After installing the library, Read the following usage criteria:

### Basic Usage

The typical usage of this library is like the following:
```
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
```

### Custom Configs

A list of a vailable configs are:

 * `LOG_FILE_FORMAT`: Log file format (default:`%Y-%m-%d`).
 * `LOG_FILE_PATH`: Logs dir absolute path and it is required (default:` `).
 * `LOG_MESSAGE_FORMAT`: Log message format (default:`{TYPE}: <{DATETIME}>  {MESSAGE}`).
 * `DATES_FORMAT`: Dates format (default:`%Y-%m-%d`).
 * `DATETIME_FORMAT`: Datetimes format (default:`%Y-%m-%d %H:%M`).
 * `PLATFORM_DATA`: Whether to activate platform data (default:`False`).
 * `ALERT_STATUS`: Email notification status (default:`False`).
 * `ALERT_SUBJECT`: Email notification subject (default:`My APP Alert`).
 * `ALERT_EMAIL`: Receiver Email or emails (format:`hello@example.com` or `hello1@example.com,hello2@example.com,..`).
 * `ALERT_TYPES`: Message types which will delivered to email (default:`['critical', 'error']`).
 * `MAILER_HOST`: SMTP server (default:`localhost`).
 * `MAILER_USER`: SMTP server user (default:`None`).
 * `MAILER_PWD`: SMTP server password (default:`None`).
 * `MAILER_FROM`: Sender email (default:`no_reply@example.com`).

To set configs in initialization:
```
import pylogging
import os

# Logs dir absolute path
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
# Create a logger instance with custom configs
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path, LOG_FILE_FORMAT='%Y-%m-%d', DATES_FORMAT='%Y-%m-%d',..,..)
# So the form will be
logger = pylogging.PyLogging(LOG_KEY_1 = 'value', LOG_KEY_2='value',..,..)
```

To set a config value:
```
logger.setConfig('CONFIG_KEY', 'config_value')
```

To get a config value:
```
logger.getConfig('CONFIG_KEY')
```

### Custom Filters

To define a filter:
```
def customFilter(type, msg):
	# Filter message text here
	return msg

filterIden = logger.addFilter(customFilter)
```

To remove a filter:
```
logger.removeFilter(filterIden)
```

### Custom Actions

To define an action:
```
def customAction(type, msg):
	# Perform any custom action here
	pass

actionIden = logger.addAction(customAction)
```

To remove an action:
```
logger.removeAction(actionIden)
```

### Email Notifications

To enable email notifications:
```
import pylogging
import os

# Logs Dir Absolute Path
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
# Create Logger Instance
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path)
# Activate email alerting
logger.setConfig('ALERT_STATUS', True)
```

Then set your own configurations like so
```
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
```

When you log messages, Messages of critical and error types will be delivered to emails:
```
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
```

Customizing
===========

Full
----


Misc
====

Changelog
---------
Version 1.0.0:
```
initial release
```

Acknowledgements
----------------

© 2015, Clivern. Released under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

**PyLogging** is authored and maintained by [@clivern](http://github.com/clivern).

 * [My website](http://clivern.com) (clivern.com)
 * [Github](http://github.com/clivern) (@clivern)
 * [Twitter](http://twitter.com/clivernco) (@clivernco)