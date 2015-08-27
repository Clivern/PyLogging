from __future__ import print_function
import os

from . import storage
from . import mailer

class PyLogging(dict, storage):
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

    def __init__(self, **kargs):
        self.logs_path = logs_path
        
    def _updateConfigs(self, **kargs):

    def __getattr__(self, name, default=False):
        """ Get attributes """
        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self:
            return self.get(name)
        else:
            # Check for denormalized name
            name = self._denormalize(name)
            if name in self:
                return self.get(name)
            else:
                return default


    def __setattr__(self, name, value):
        """ Set attributes """
        if name in self.__dict__:
            self.__dict__[name] = value
        elif name in self:
            self[name] = value
        else:
            # Check for denormalized name
            name2 = self._normalize(name)
            if name2 in self:
                self[name2] = value
            else:
                # New attribute
                self[name] = value


    def _normalize(self, value):
        """ Normalize a string """

        if value.find('-') != -1:
            value = value.replace('-', '_')

        return value


    def _denormalize(self, value):
        """ De-normalize a string """

        if value.find('_') != -1:
            value = value.replace('_', '-')

        return value


    def addFilter(self, filter, types = ['info', 'warning', 'error', 'critical', 'log']):
        pass

    def removeFilter(self, filter):
        pass    

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

    def critical(self, msg):
        pass

    def log(self, msg):
        pass
