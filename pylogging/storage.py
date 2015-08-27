

class JsonStorage():

	def save(self):
		""" Save message to .json file """
		return True

class TextStorage():

	def save(self):
		""" Save message to .text file """
		return True


class YamlStorage():

	def save(self):
		""" Save message to .yaml file """
		return True

class IniStorage():

	def save(self):
		""" Save message to .ini file """
		return True

class Storage():

	def __init__(self, log_file):
		""" Init storage class with requested storage type """
		if log_file.endswith('.json'):
			self.storage = JsonStorage()
		elif log_file.endswith('.text'):
			self.storage = TextStorage()
		elif log_file.endswith('.yaml'):
			self.storage = YamlStorage()
		elif log_file.endswith('.ini'):
			self.storage = IniStorage()
		else:
			 raise Exception('Error Configuring PyLogger.Storage Class')

	def store(self, msg):
		""" Store message in requested storage type """
		return self.storage.save(msg)	