
class TextStorage():
    """ Text Storage Class """
    
    def write(self, log_file, msg):
        """ Write message to .txt file """
        with open(log_file, 'a') as LogFile:
            LogFile.write(msg + os.linesep)

    def read(self, log_file):
        """ Read messages from .txt file """
        if os.path.isfile(log_file):
            with open(log_file, 'r') as LogFile:
                data = LogFile.readlines()
                data = "".join(line for line in data)
        else:
            data = ''
        return data

class Storage():
    """ PyLogger Storage Class """

    def __init__(self, log_file):
        """ Init storage class wth requested storage type """
        self.LOG_FILE = log_file
        if self.LOG_FILE.endswith('.txt'):
            self.storage = TextStorage()
        else:
            raise Exception('Error Configuring PyLogger.Storage Class')

    def write(self, msg):
        """ Store message in requested storage type """
        return self.storage.write(self.LOG_FILE, msg)

    def read(self):
        """ Read messages from requested storage type """
        return self.storage.read(self.LOG_FILE)