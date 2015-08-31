"""
Python Logging Library

@author: Clivern U{hello@clivern.com}
"""
import os


class TextStorage():
    """ Text Storage Class """
    
    def write(self, log_file, msg):
        """ Append message to .log file """
        try:
            with open(log_file, 'a') as LogFile:
                LogFile.write(msg + os.linesep)
        except:
            raise Exception('Error Configuring PyLogger.TextStorage Class.')

        return os.path.isfile(log_file)

    def read(self, log_file):
        """ Read messages from .log file """
        if os.path.isdir(os.path.dirname(log_file)) and os.path.isfile(log_file):
            with open(log_file, 'r') as LogFile:
                data = LogFile.readlines()
                data = "".join(line for line in data)
        else:
            data = ''
        return data


class Storage():
    """ PyLogger Storage Class """

    def __init__(self, log_file):
        """ Init Storage Class with Requested Storage Type """

        # Log File Path
        self.LOG_FILE = log_file

        # Create Log File and Dirs
        if os.path.isdir(os.path.dirname(self.LOG_FILE)) == False:
            try:
                # Dirs not exist, Create them
                os.makedirs(os.path.dirname(self.LOG_FILE))
            except:
                # Error Create Dirs
                raise Exception('Error Creating Log File Path.')
            
        # Check if Storage is .log File
        if self.LOG_FILE.endswith('.log'):
            self.storage = TextStorage()
        else:
            # Storage type is incorrect
            raise Exception('Error Configuring PyLogger.Storage Class.')

    def write(self, msg):
        """ Append message to Requested Storage Type """
        return self.storage.write(self.LOG_FILE, msg)

    def read(self):
        """ Read messages from Requested Storage Type """
        return self.storage.read(self.LOG_FILE)