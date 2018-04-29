from requests import get
from bs4 import BeautifulSoup
from alert import Alert
import pdb #pdb.set_trace()
class Scraper():
	
	def __init__(self,url):
		self.url = url
	
	def get_content(self):
		html = get(self.url, stream=True)
		return html
			
	def setSectionObject(self):
		content = self.get_content().text
		self.bs4_content = BeautifulSoup(content, 'html.parser')
		self.get_alerts(self.bs4_content)
		#self.get_watches(self.bs4_content)
		#self.get_warnings(self.bs4_content)
	
	def get_alerts(self, content):
		array = []
		alerts = content.find(id="alert")
		if alerts and len(alerts):
			alerts = alerts.find(class_="list-block").children
			for alert in alerts:
				if alert != '\n':
					description, link, date = self.parse_content(alert)
					new_alert = Alert(description, link)
					new_alert.save_alert()
					
	def get_watches(self, content):
		watches = content.find(id="watches")
		if watches and len(watches):
			watches = watches.find(class_="list-block").children
			for watch in watches:
				if alert != '\n':
					description, link, date = self.parse_content(watch)
			print("Watches----------")
			print(description)
			print('-------------------')
			print(link)
			print('-------------------')
			print(date)
			
	def get_warnings(self, content):
		warnings = content.find(id="warn")
		if warnings and len(warnings):
			warnings = warnings.find(class_="list-block").children
			for warn in warnings:
				if alert != '\n':
					description, link, date = self.parse_content(warn)
			print("Warnings------------")
			print(description)
			print('-------------------')
			print(link)
			print('-------------------')
			print(date)
			
	def parse_content(self, section):
		description,link,readme = section.find_all('a')
		date = section.find_all(class_='date')[0].contents[0]
		return [description.find(id='SearchPanel').contents[0], link['href'], date] 
		

#BeautifulSoup
 #soup = BeautifulSoup(htmltext, parser)
 #soup.find(id='alert')
 