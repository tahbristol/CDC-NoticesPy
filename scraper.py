from requests import get 
import pdb 
class Scraper():
	
	def __init__(self,url):
		self.url = url
	
	def get_content(self):
		html = get(self.url, stream=True)
		return html
			
	def setSectionObject(self):
		content = self.get_content().text
		