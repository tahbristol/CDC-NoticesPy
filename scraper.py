from requests import get 

class Scraper():
	
	def __init__(self,url):
		self.url = url
	
	def get_content(self):
			html = get(self.url, stream=True)
			return html.text