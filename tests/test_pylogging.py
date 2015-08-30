from __future__ import print_function
from time import gmtime, strftime
import pylogging
import unittest
import os
import datetime

class TestPyLoggingMethods(unittest.TestCase):

	def test_configs(self):
		""" Test Configurations Getters and Setters """
		self._logger = pylogging.PyLogging( LOG_FILE_FORMAT = 1, LOG_FILTE_PATH = 2, LOG_MESSAGE_FORMAT = 3, DATES_FORMAT = 4, DATETIME_FORMAT = 5, PLATFORM_DATA = 6, ALERT_STATUS = 7, ALERT_SUBJECT = 8, ALERT_EMAIL = 9, ALERT_TYPES = 10, MAILER_HOST = 11, MAILER_USER = 12, MAILER_PWD = 13, MAILER_FROM = 14)
		self.assertEqual(self._logger.getConfig('LOG_FILE_FORMAT'), 1)
		self.assertEqual(self._logger.getConfig('LOG_FILTE_PATH'), 2)
		self.assertEqual(self._logger.getConfig('LOG_MESSAGE_FORMAT'), 3)
		self.assertEqual(self._logger.getConfig('DATES_FORMAT'), 4)
		self.assertEqual(self._logger.getConfig('DATETIME_FORMAT'), 5)
		self.assertEqual(self._logger.getConfig('PLATFORM_DATA'), 6)
		self.assertEqual(self._logger.getConfig('ALERT_STATUS'), 7)
		self.assertEqual(self._logger.getConfig('ALERT_SUBJECT'), 8)
		self.assertEqual(self._logger.getConfig('ALERT_EMAIL'), 9)
		self.assertEqual(self._logger.getConfig('ALERT_TYPES'), 10)
		self.assertEqual(self._logger.getConfig('MAILER_HOST'), 11)
		self.assertEqual(self._logger.getConfig('MAILER_USER'), 12)
		self.assertEqual(self._logger.getConfig('MAILER_PWD'), 13)
		self.assertEqual(self._logger.getConfig('MAILER_FROM'), 14)
		self._logger.setConfig('MAILER_FROM', 15)
		self.assertEqual(self._logger.getConfig('MAILER_FROM'), 15)

	def test_logger(self):
		""" Test Logger Class """
		
		now = datetime.datetime.now()
		log_path = os.path.dirname(os.path.abspath(__file__)) + '/' + now.strftime('%Y-%m-%d') + '.log'

		if os.path.isfile(log_path):
			os.remove(log_path)

		self._logger = pylogging.PyLogging(LOG_FILTE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/')
		self._logger.info("Line1.")
		self._logger.warning("Line2.")
		self._logger.error("Line3.")
		self._logger.critical("Line4.")
		self._logger.log("Line5.")
		
		
		with open(log_path, 'r') as LogFile:
			data = LogFile.readlines()
			data = [item for item in data if item != '\n']

		self.assertEqual(data[0], 'INFO: <2015-08-30>  Line1.\n')
		self.assertEqual(data[1], 'WARNING: <2015-08-30>  Line2.\n')
		self.assertEqual(data[2], 'ERROR: <2015-08-30>  Line3.\n')
		self.assertEqual(data[3], 'CRITICAL: <2015-08-30>  Line4.\n')
		self.assertEqual(data[4], 'LOG: <2015-08-30>  Line5.\n')

		if os.path.isfile(log_path):
			os.remove(log_path)

if __name__ == '__main__':
    unittest.main()