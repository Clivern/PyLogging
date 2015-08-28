from __future__ import print_function
from time import gmtime, strftime
import os


class PyLogging(dict):
    """ A custom logger class """
    
    LOG_FILE_FORMAT = 'YYYY-MM-DD'
    LOG_MESSAGE_FORMAT = '{DATE} {TYPE} {MESSAGE}'
    STORAGE_TYPE = 'text'
    DATES_FORMAT = 'YYYY-MM-DD'
    DATETIME_FORMAT = 'YYYY-MM-DD HH:MM:SS'
    DEFAULT_TIMEZONE = 'America/New York'
    
    ALERT_STATUS = False
    ALERT_EMAIL = 'hello@example.com'
    ALERT_TYPES = ['critical', 'error']

    FILTERS = []
    ACTIONS = []

    def __init__(self, **kargs):
        self._config(**kargs)

    def _config(self, **kargs):
        for key, value in kargs.items():
            setattr(self, key, value)

    def getConfig(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return False

    def setConfig(self, key, value):
        setattr(self, key, value)
        return True

    def addFilter(self, filter):
        self.FILTERS.append(filter)
        return "FILTER#{}".format(len(self.FILTERS) - 1)

    def addAction(self, action):
        self.ACTIONS.append(action)
        return "ACTION#{}".format(len(self.ACTIONS) - 1)

    def _execFilters(self, type, msg):
        for filter in self.FILTERS:
            msg = filter(type, msg)
        return msg

    def _execActions(self, type, msg):
        for action in self.ACTIONS:
            action(type, msg)

    def removeFilter(self, filter):
        filter = filter.split('#')
        del self.FILTERS[filter[1]]
        return True

    def removeAction(self, action):
        action = action.split('#')
        del self.ACTIONS[action[1]]
        return True

    def info(self, msg):
        self._execActions('info', msg)
        msg = self._execFilters('info', msg)
        return msg

    def warning(self, msg):
        self._execActions('warning', msg)
        msg = self._execFilters('warning', msg)

    def error(self, msg):
        self._execActions('error', msg)
        msg = self._execFilters('error', msg)

    def critical(self, msg):
        self._execActions('critical', msg)
        msg = self._execFilters('critical', msg)

    def log(self, msg):
        self._execActions('log', msg)
        msg = self._execFilters('log', msg)