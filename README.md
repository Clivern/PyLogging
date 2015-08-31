PyLogging
=========

PyLogging is a light-weight python logging library. It provides ability to write logs in your own customized format. It also provide support for custom logs filters, custom actions and email notifications.

*Current version: [v1.0.0]*
[![Build Status](https://travis-ci.org/Clivern/PyLogging.svg?branch=master)](https://travis-ci.org/Clivern/PyLogging)

Installation
------------
To install PyLogging run this command:
```
pip install pylogging
```
or [download](https://github.com/Clivern/PyLogging/archive/master.zip) Package then run this command:
```
pip install PyLogging-master.zip
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
- `LOG_FILE_FORMAT`:
- `LOG_FILE_PATH`:
- `LOG_MESSAGE_FORMAT`:
- `DATES_FORMAT`:
- `DATETIME_FORMAT`:
- `PLATFORM_DATA`:
- `ALERT_STATUS`:
- `ALERT_SUBJECT`:
- `ALERT_EMAIL`:
- `ALERT_TYPES`:
- `MAILER_HOST`:
- `MAILER_USER`:
- `MAILER_PWD`:
- `MAILER_FROM`: 

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
<!--
### Email Notifications

To enable email notifications:
```

```
-->
<!--
Customizing
===========

Basic
-----

Full
----

-->
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