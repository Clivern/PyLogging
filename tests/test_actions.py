from __future__ import print_function
from time import gmtime, strftime
import pylogging
import unittest
import os
import datetime

class TestPyLoggingMethods(unittest.TestCase):

	def test_actions(self):
		""" Test Logger Class """
		
		now = datetime.datetime.now()
		log_path = os.path.dirname(os.path.abspath(__file__)) + '/' + now.strftime('%Y-%m-%d') + '.log'

		if os.path.isfile(log_path):
			os.remove(log_path)

		self._logger = pylogging.PyLogging(LOG_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/')
		self._count = 0
		actionAdded = self._logger.addAction(self._actionAdded)
		actionRemoved = self._logger.addAction(self._actionRemoved)
		filterAdded = self._logger.addFilter(self._filterAdded)
		filterRemoved = self._logger.addFilter(self._filterRemoved)
		self._logger.removeFilter(filterRemoved)
		self._logger.removeAction(actionRemoved)
		self._logger.info("Line1.")
		self._logger.warning("Line2.")
		self._logger.error("Line3.")
		self._logger.critical("Line4.")
		self._logger.log("Line5.")
		
		with open(log_path, 'r') as LogFile:
			data = LogFile.readlines()
			data = [item.rstrip() for item in data if item != '\n']

		self.assertEqual(data[0], 'INFO: <'+ now.strftime('%Y-%m-%d %H:%M') +'>  Line1.info'.rstrip())
		self.assertEqual(data[1], 'WARNING: <'+ now.strftime('%Y-%m-%d %H:%M') +'>  Line2.warning'.rstrip())
		self.assertEqual(data[2], 'ERROR: <'+ now.strftime('%Y-%m-%d %H:%M') +'>  Line3.error'.rstrip())
		self.assertEqual(data[3], 'CRITICAL: <'+ now.strftime('%Y-%m-%d %H:%M') +'>  Line4.critical'.rstrip())
		self.assertEqual(data[4], 'LOG: <'+ now.strftime('%Y-%m-%d %H:%M') +'>  Line5.log'.rstrip())
		self.assertEqual(self._count, 5)

		if os.path.isfile(log_path):
			os.remove(log_path)

	def _filterAdded(self, type, msg):
		return msg + type

	def _filterRemoved(self, type, msg):
		return msg + type

	def _actionAdded(self, type, msg):
		self._count += 1

	def _actionRemoved(self, type, msg):
		self._count += 1

if __name__ == '__main__':
    unittest.main()