import unittest
from scraper import Scraper

class ScraperTest(unittest.TestCase):
	
	def setUp(self):
		self.new_scraper = Scraper('http://www.tahbristol.com')
		self.response = self.new_scraper.get_content()
		
		
	def testResponse(self):
		self.assertEqual(self.response.status_code, 200)
		

if __name__ == '__main__':
    unittest.main()