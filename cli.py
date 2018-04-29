import click 
from scraper import Scraper
from notice import Notice
from requests.exceptions import RequestException 
from contextlib import closing 
from bs4 import BeautifulSoup

scraper = Scraper('https://wwwnc.cdc.gov/travel/notices')
scraper.get_content()
scraper.setSectionObject()

print("Hello, Welcome to CDC Notices")
print("Enter a command to get health travel advisories")
print("Type 'help' to get a list of commands")






