from unittest import TestCase

from project_finder import *

class TestProjectFinder(TestCase):

		def testBuildRootUrl(self):
				"""Test that a simple url is built correctly
				"""

				url = 'https://github.com/CodeClub/scratch-curriculum/blob/master/'
				directory = 'en-GB/Additional Projects/Christmas Capers'
				filename = 'xmas-final.png'

				result = 'https://github.com/CodeClub/scratch-curriculum/blob/master/en-GB/Additional%20Projects/Christmas%20Capers/xmas-final.png'
				self.assertEqual(result,build_root_url(url,directory,filename))