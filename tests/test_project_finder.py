from unittest import TestCase

from project_finder import *

class TestProjectFinder(TestCase):

	def testBuildRootUrl(self):
		"""Test that a simple url is built correctly
		"""

		url = 'https://github.com/CodeClub/scratch-curriculum/blob/master/'
		filename = 'xmas-final.png'

		result = 'https://github.com/CodeClub/scratch-curriculum/blob/master/xmas-final.png'
		self.assertEqual(result,build_root_url(url,filename))