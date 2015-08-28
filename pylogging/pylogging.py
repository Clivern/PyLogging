from __future__ import print_function
from time import gmtime, strftime
import os

class PyLogging(dict):
    """ A Custom Logger Class """
    
    LOG_FILE_FORMAT = 'YYYY-MM-DD'
    LOG_MESSAGE_FORMAT = '{TYPE}: <{DATE}> {MESSAGE}'
    DATES_FORMAT = 'YYYY-MM-DD'
    DATETIME_FORMAT = 'YYYY-MM-DD HH:MM:SS'
    DEFAULT_TIMEZONE = 'America/New York'
    
    """" Mailer Custom Configs """
    ALERT_SUBJECT = "My APP Alert"
    ALERT_STATUS = False
    ALERT_EMAIL = 'hello@example.com'
    ALERT_TYPES = ['critical', 'error']
    MAILER_HOST = 'localhost'
    MAILER_USER = None
    MAILER_PWD = None
    MAILER_FROM = 'no_reply@example.com'
    MAILER_TO = 'admin@example.com'

    """ Custom Filters and Actions """
    FILTERS = []
    ACTIONS = []

    def __init__(self, **kargs):
        self._config(**kargs)
        self._configMailer()

    def _config(self, **kargs):
        """ Reconfigure Library """
        for key, value in kargs.items():
            setattr(self, key, value)

    def getConfig(self, key):
        """ Get Config Value """
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return False

    def setConfig(self, key, value):
        """ Set Config Value """
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

    def _execFilters(self, type, msg):
        """ Execute Registered Filters """
        for filter in self.FILTERS:
            msg = filter(type, msg)
        return msg

    def _execActions(self, type, msg):
        """ Execute Registered Actions """
        for action in self.ACTIONS:
            action(type, msg)

    def removeFilter(self, filter):
        """ Remove Registered Filter """
        filter = filter.split('#')
        del self.FILTERS[filter[1]]
        return True

    def removeAction(self, action):
        """ Remove Registered Action """
        action = action.split('#')
        del self.ACTIONS[action[1]]
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

    def _processMsg(type, msg):
        """ Process Debug Messages """
        log_file = "2012-10-2"
        self._STORAGE = Storage(log_file)
        return self._STORAGE.write(msg)

    def _configMailer():
        """ Config Mailer Class """
        self._MAILER = Mailer(self.MAILER_HOST)
        self._MAILER.login(self.MAILER_USER, self.MAILER_PWD)

    def _sendMsg(self, type, msg):
        """ Send Alert Message To Emails """
        if ALERT_STATUS and type in self.ALERT_TYPES:
            self._MAILER.send(self, MAILER_FROM, MAILER_TO, self.ALERT_SUBJECT, msg)