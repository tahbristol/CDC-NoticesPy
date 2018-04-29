import pdb

class Notice():
	notices = []
	
	def __init__(self, notice_type, description, readme_link, date):
		self.notice_type = notice_type 
		self.description = description
		self.readme_link = readme_link
		self.date = date
		self.title = self.get_title()
		
	def get_title(self):
		title = ''
		for word in self.readme_link.split('/')[-1].split('-'):
			title += " " + word.capitalize()
		return title.strip()
	
	def save_notice(self):
		Notice.notices.append(self)
	
	@classmethod
	def all_notices(self):
		index = 1
		for notice in self.notices:
			print(f"{index}.")
			print(notice.date)
			print(notice.title)
			print(notice.description)
			print(notice.readme_link)
			print(notice.notice_type)
			print("***********************")
			index += 1
		
	@classmethod
	def choose_notice(self, notice_type):
		index = 1
		for notice in self.notices:
			if notice.notice_type == notice_type:
				print(f"{index}.")
				print(notice.date)
				print(notice.title)
				print(notice.description)
				print(notice.readme_link)
				print(notice.notice_type)
				print("***********************")
				index += 1
				