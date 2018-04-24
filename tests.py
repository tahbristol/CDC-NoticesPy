import unittest
from scraper import Scraper
from alert import Alert

class ScraperTest(unittest.TestCase):
	
	def setUp(self):
		self.new_scraper = Scraper('http://www.tahbristol.com')
		self.response = self.new_scraper.get_content()
		
		
	def testResponse(self):
		self.assertEqual(self.response.status_code, 200)
		

class AlertTest(unittest.TestCase):
	
	def setUp(self):
		self.new_alert = Alert('alert1', 'summary1', 'readme1')
		
	def testAlert(self):
		self.assertEqual(self.new_alert.title, 'alert1')
		

if __name__ == '__main__':
    unittest.main()