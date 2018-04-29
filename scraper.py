from requests import get
from bs4 import BeautifulSoup
from notice import Notice
import pdb #pdb.set_trace()
class Scraper():
	
	def __init__(self,url):
		self.url = url
	
	def get_content(self):
		html = get(self.url, stream=True)
		return html
			
	def setSectionObject(self):
		notice_types = ["alert", "warn", "watch"]
		content = self.get_content().text
		self.bs4_content = BeautifulSoup(content, 'html.parser')
		for notice_type in notice_types:
			self.get_notice(self.bs4_content, notice_type)
	
	def get_alerts(self, content):
		array = []
		alerts = content.find(id="alert")
		if alerts and len(alerts):
			alerts = alerts.find(class_="list-block").children
			for alert in alerts:
				if alert != '\n':
					description, link, date = self.parse_content(alert)
					new_alert = Alert(description, link)
					new_alert.save()
			
	def get_notice(self, content, notice_type):
		class_name = notice_type.capitalize()	
		notices = content.find(id=notice_type)
		if notices and len(notices):
			notices = notices.find(class_="list-block").children
			for notice in notices:
				if notice != '\n':
					description, link, date = self.parse_content(notice)
					new_notice = Notice(notice_type, description, link, date)
					new_notice.save_notice()
			
	def parse_content(self, section):
		description,link,readme = section.find_all('a')
		date = section.find_all(class_='date')[0].contents[0]
		return [description.find(id='SearchPanel').contents[0], link['href'], date] 
		

#BeautifulSoup
 #soup = BeautifulSoup(htmltext, parser)
 #soup.find(id='alert')
 