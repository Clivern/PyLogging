PyLogging
=========

PyLogging is a light-weight python logging library. It provides ability to write logs in your own customized format. It is also provides support for custom log filters, custom log actions and email notifications.

*Current version: [v1.0.2]*

[![Build Status](https://travis-ci.org/Clivern/PyLogging.svg?branch=master)](https://travis-ci.org/Clivern/PyLogging)
[![PyPI version](https://badge.fury.io/py/PyLogging.svg)](https://badge.fury.io/py/PyLogging)

Installation
------------
To install PyLogging run this command:
```
pip install pylogging
```
or [download](https://github.com/Clivern/pylogging/archive/1.0.2.zip) Package then run this command:
```
pip install PyLogging-1.0.2.zip
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
 * `ALERT_EMAIL`: Receiver Email or emails (format:`you@gmail.com` or `you@gmail.com,other@gmail.com,..`).
 * `ALERT_TYPES`: Message types which will delivered to email (default:`['critical', 'error']`).
 * `MAILER_HOST`: SMTP server (default:`smtp.gmail.com`).
 * `MAILER_PORT`: SMTP server port (default:`587`).
 * `MAILER_USER`: SMTP server user (default:`None`).
 * `MAILER_PWD`: SMTP server password (default:`None`).
 * `MAILER_FROM`: Sender email (default:`you@gmail.com`).

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

So if you like to send alert to `you@gmail.com` and your email password is `dummypass` the library configs will be:
```
logs_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/'
logger = pylogging.PyLogging(LOG_FILE_PATH = logs_path)
logger.setConfig('ALERT_STATUS', True)
logger.setConfig('ALERT_SUBJECT', "My APP Alert")
logger.setConfig('ALERT_EMAIL', 'you@gmail.com')
logger.setConfig('ALERT_TYPES', ['critical', 'error'])
logger.setConfig('MAILER_HOST', 'smtp.gmail.com')
logger.setConfig('MAILER_PORT', 587)
logger.setConfig('MAILER_USER', 'you@gmail.com')
logger.setConfig('MAILER_PWD', 'dummypass')
logger.setConfig('MAILER_FROM', 'you@gmail.com')

logger.info("Info Message")
logger.log("Normal Log Message.")
logger.warning("Warning Message.")
logger.error("Error Message.")
logger.critical("Critical Message.")
```

Customizing
===========

Log File
--------
Since log file name passes through `strftime(format)`, You can change file name into any valid time format string. For more info about [format strings](https://docs.python.org/2/library/time.html#time.strftime).
```
logger.setConfig('LOG_FILE_FORMAT', '%y-%m-%d')
```

Log Message
-----------
By default you can use combination of available vars in log message format:

 * `{TYPE}`: Log message type.
 * `{DATE}`: Log time date.
 * `{DATETIME}`: Log time datetime.
 * `{MESSAGE}`: Log message content.

The default format is `{TYPE}: <{DATETIME}>  {MESSAGE}`, You can change like the following:
```
logger.setConfig('LOG_MESSAGE_FORMAT', '{DATE}: {TYPE}-{MESSAGE}')
```

To add additional platform vars. You need to activate them:
```
logger.setConfig('PLATFORM_DATA', True)
```

This will allow usage of:

 * `PL_TYPE`: The machine type, e.g. `i386`
 * `PL_NAME`: The computer’s network name.
 * `PL_PROCESSOR`: The (real) processor name, e.g. `amdk6`.
 * `PL_PY_BUILD_DATE`: The Python build number.
 * `PL_PY_COMPILER`: A string identifying the compiler used for compiling Python.
 * `PL_PY_RELEASE`: The system’s release, e.g. `2.2.0`.
 * `PL_OS`: The system/OS name, e.g. `Linux`, `Windows`
 * `PL_TIMEZONE`: The system timezone.

For example we can customize message format into:
```
logger.setConfig('PLATFORM_DATA', True)
logger.setConfig('LOG_MESSAGE_FORMAT', '{DATE}-{PL_OS}: {TYPE} - {MESSAGE}')
```
and so on.


Misc
====

Changelog
---------
Version 1.0.2:
```
Bug Fixes and docs enhancements.
```
Version 1.0.1:
```
Mailer class fixed.
```
Version 1.0.0:
```
initial release
```

Acknowledgements
----------------

© 2015, Clivern. Released under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

**PyLogging** is authored and maintained by [@clivern](http://github.com/clivern).
