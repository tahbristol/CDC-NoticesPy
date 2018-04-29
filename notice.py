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
		return self.notices
	
	
		