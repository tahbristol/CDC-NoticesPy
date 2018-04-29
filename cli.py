import click 
from scraper import Scraper
from notice import Notice
from requests.exceptions import RequestException 
from contextlib import closing 
import webbrowser
from bs4 import BeautifulSoup

class Cli():
	def __init__(self):
		print("Hello, Welcome to CDC Notices")
		print("Enter a command to get health travel advisories")
		print("Type 'help' to get a list of commands")
		
		
		scraper = Scraper('https://wwwnc.cdc.gov/travel/notices')
		scraper.get_content()
		scraper.setSectionObject()
	
	def call(self):
		user_command = ''
		
		while user_command != 'exit':
			user_command = input("Enter the a command to get health travel advisories.\nType help for a list of commands.\n>")
			if user_command == 'alerts':
				self.get_alerts()
			elif user_command == 'warnings':
				self.get_warnings()
			elif user_command == 'watches':
				self.get_watches()
			elif user_command == 'help':
				self.help()
			elif user_command == 'all':
				self.all_notices()
			elif user_command == 'readmore':
				read_notice = input("Type the number of the notice from the list of 'all notices'.")
				self.readmore(read_notice)
			elif user_command == 'exit':
				print("Goodbye")
				break
			else:
				user_command = input("Enter the a command to get health travel advisories.\nType help for a list of commands.\n>")

	def get_alerts(self):
		Notice.choose_notice("alert")
	
	def get_warnings(self):
		Notice.choose_notice("warn")
	
	def get_watches(self):
		Notice.choose_notice("watch")
	
	def all_notices(self):
		Notice.all_notices()
		
	def readmore(self, notice_number):
		base = 'https://wwwnc.cdc.gov/travel/notices/'
		notice = Notice.notices[int(notice_number) - 1]
		notice_url = notice.title.replace(' ', '-').lower()
		url = f"{base}{notice.notice_type}/{notice_url}"
		webbrowser.open(url)
		
	def help(self):
		print("*****************************")
		print("all: Display all notices")
		print("alerts: Display alerts only.")
		print("warnings: Display warnings only.")
		print("watches: Display watches only.")
		print("readmore: open readmore in browser. 'readmore' press enter then enter the number corresponding to the notice you want")
		print("exit: exit the application")
		print("******************************")


