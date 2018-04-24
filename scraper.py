from requests import get
from bs4 import BeautifulSoup
import pdb 
class Scraper():
	
	def __init__(self,url):
		self.url = url
	
	def get_content(self):
		html = get(self.url, stream=True)
		return html
			
	def setSectionObject(self):
		content = self.get_content().text
		self.bs4Content = BeautifulSoup(content, 'html.parser')



#BeautifulSoup
 #soup = BeautifulSoup(htmltext, parser)
 #soup.find(id='alert')
 