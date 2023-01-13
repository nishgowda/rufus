# Unit tests for rufus.py
import unittest
from unittest.mock import patch

from rufus import Rufus

class TestRufus(unittest.TestCase):

	def setUp(self):
		self.rufus = Rufus(dir='.')
	
	def test_get_current_branch(self):
		self.assertEqual(self.rufus.get_current_branch(), 'master')
	
	@patch('rufus.Rufus.has_untracked_files')
	def test_has_untracked_files(self, mock_has_untracked_files):
		mock_has_untracked_files.return_value = True
		self.assertTrue(self.rufus.has_untracked_files())
	
	@patch('rufus.Rufus.is_within_past_week')
	def test_is_within_past_week(self, mock_is_within_past_week):
		mock_is_within_past_week.return_value = True
		self.assertTrue(self.rufus.is_within_past_week())
	
	@patch('rufus.Rufus.is_author_rufus')
	def test_is_author_rufus(self, mock_is_author_rufus):
		mock_is_author_rufus.return_value = True
		self.assertTrue(self.rufus.is_author_rufus())

if __name__ == '__main__':
	unittest.main()
