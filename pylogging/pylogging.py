"""
Python Logging Library

@author: Clivern U{hello@clivern.com}
"""
from __future__ import print_function
from time import gmtime, strftime
import platform
import os
import datetime
from .mailer import Mailer
from .storage import Storage


class PyLogging(dict):
    """ A Custom Logger Class """
    
    # Log File Name Format    
    LOG_FILE_FORMAT = '%Y-%m-%d'

    # Log File Path
    LOG_FILE_PATH = ''
    
    # Message Format. A list of available vars: 
    #   TYPE: Message type
    #   DATE: Log time Date
    #   DATETIME: Log time datetime
    #   MESSAGE: Message content
    LOG_MESSAGE_FORMAT = '{TYPE}: <{DATETIME}>  {MESSAGE}'
    
    # Dates Format
    DATES_FORMAT = '%Y-%m-%d'
    
    # Datetime Format
    DATETIME_FORMAT = '%Y-%m-%d %H:%M'

    # Platform Data Vars
    #  If set to true, It will Add the following:
    #   PL_TYPE: The machine type, e.g. i386
    #   PL_NAME: The computer network name.
    #   PL_PROCESSOR: The (real) processor name, e.g. amdk6.
    #   PL_PY_BUILD_DATE: The Python build number.
    #   PL_PY_COMPILER: A string identifying the compiler used for compiling Python.
    #   PL_PY_RELEASE: The system release, e.g. 2.2.0.
    #   PL_OS: The system/OS name, e.g. Linux, Windows
    #   PL_TIMEZONE: The system timezone.
    PLATFORM_DATA = False

    # Whether to Send Alert Email
    ALERT_STATUS = False
    
    # Alert Email Default Subject
    ALERT_SUBJECT = "My APP Alert"

    # Alert Email
    ALERT_EMAIL = 'you@gmail.com'
    
    # Message Types to Send to Email
    ALERT_TYPES = ['critical', 'error']

    # Mailer Class Host
    MAILER_HOST = 'smtp.gmail.com'

    # Mailer Class Port
    MAILER_PORT = 587
    
    # Mailer Class User
    MAILER_USER = None

    # Mailer Class PWD
    MAILER_PWD = None

    # From Email Value
    MAILER_FROM = 'you@gmail.com'

    # Custom Message Filters
    FILTERS = []

    # Custom Message Actions
    ACTIONS = []

    def __init__(self, **kargs):
        """ Init PyLogger Class and Mailer Class """
        self._config(**kargs)

    def _config(self, **kargs):
        """ ReConfigure Package """
        for key, value in kargs.items():
            setattr(self, key, value)

    def getConfig(self, key):
        """ Get a Config Value """
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return False

    def setConfig(self, key, value):
        """ Set a Config Value """
        setattr(self, key, value)
        return True

    def addFilter(self, filter):
        """ Register Custom Filter """
        self.FILTERS.append(filter)
        return "FILTER#{}".format(len(self.FILTERS) - 1)

    def addAction(self, action):
        """ Register Custom Action """
        self.ACTIONS.append(action)
        return "ACTION#{}".format(len(self.ACTIONS) - 1)

    def removeFilter(self, filter):
        """ Remove Registered Filter """
        filter = filter.split('#')
        del self.FILTERS[int(filter[1])]
        return True

    def removeAction(self, action):
        """ Remove Registered Action """
        action = action.split('#')
        del self.ACTIONS[int(action[1])]
        return True

    def info(self, msg):
        """ Log Info Messages """
        self._execActions('info', msg)
        msg = self._execFilters('info', msg)
        self._processMsg('info', msg)
        self._sendMsg('info', msg)

    def warning(self, msg):
        """ Log Warning Messages """
        self._execActions('warning', msg)
        msg = self._execFilters('warning', msg)
        self._processMsg('warning', msg)
        self._sendMsg('warning', msg)

    def error(self, msg):
        """ Log Error Messages """
        self._execActions('error', msg)
        msg = self._execFilters('error', msg)
        self._processMsg('error', msg)
        self._sendMsg('error', msg)

    def critical(self, msg):
        """ Log Critical Messages """
        self._execActions('critical', msg)
        msg = self._execFilters('critical', msg)
        self._processMsg('critical', msg)
        self._sendMsg('critical', msg)

    def log(self, msg):
        """ Log Normal Messages """
        self._execActions('log', msg)
        msg = self._execFilters('log', msg)
        self._processMsg('log', msg)
        self._sendMsg('log', msg)

    def _processMsg(self, type, msg):
        """ Process Debug Messages """
        now = datetime.datetime.now()

        # Check If Path not provided
        if self.LOG_FILE_PATH == '':
            self.LOG_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'

        # Build absolute Path
        log_file = self.LOG_FILE_PATH + now.strftime(self.LOG_FILE_FORMAT) + '.log'
        
        # Add General Vars
        msg = self.LOG_MESSAGE_FORMAT.format(
            TYPE=type.upper(),
            DATE=now.strftime(self.DATES_FORMAT),
            DATETIME=now.strftime(self.DATETIME_FORMAT),
            MESSAGE=msg,
        )

        # Check if to add platform data
        if self.PLATFORM_DATA:
            # Add Platform Specific Vars
            msg = msg.format(
                PL_TYPE=platform.machine(),
                PL_NAME=platform.node(),
                PL_PROCESSOR=platform.processor(),
                PL_PY_BUILD_DATE=platform.python_build()[1],
                PL_PY_COMPILER=platform.python_compiler(),
                PL_PY_RELEASE=platform.release(),
                PL_OS=platform.system(),
                PL_TIMEZONE=strftime("%z", gmtime())
            )

        # Create Storage Instance
        self._STORAGE = Storage(log_file)
        # Write Storage
        return self._STORAGE.write(msg)

    def _configMailer(self):
        """ Config Mailer Class """
        self._MAILER = Mailer(self.MAILER_HOST, self.MAILER_PORT)
        self._MAILER.login(self.MAILER_USER, self.MAILER_PWD)

    def _sendMsg(self, type, msg):
        """ Send Alert Message To Emails """
        if self.ALERT_STATUS and type in self.ALERT_TYPES:
            self._configMailer()
            self._MAILER.send(self.MAILER_FROM, self.ALERT_EMAIL, self.ALERT_SUBJECT, msg)

    def _execFilters(self, type, msg):
        """ Execute Registered Filters """
        for filter in self.FILTERS:
            msg = filter(type, msg)
        return msg

    def _execActions(self, type, msg):
        """ Execute Registered Actions """
        for action in self.ACTIONS:
            action(type, msg)