import click 
from scraper import Scraper
from alert import Alert
from requests.exceptions import RequestException 
from contextlib import closing 
from bs4 import BeautifulSoup

print("Hello, Welcome to CDC Notices")
print("Enter a command to get health travel advisories")
print("Type 'help' to get a list of commands")

scraper = Scraper('https://wwwnc.cdc.gov/travel/notices')
scraper.get_content()
scraper.setSectionObject()
for alert in Alert.all_alerts(Alert):
	print(alert.get_title)




