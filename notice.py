class Notice():
	all_notices = []
	alert_notices = []
	warn_notices = []
	watch_notices = []
	
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
		if self.notice_type == 'alert':
			Notice.alert_notices.append(self)
		if self.notice_type == 'warn':
			Notice.warn_notices.append(self)
		if self.notice_type == 'watch':
			Notice.watch_notices.append(self)
		Notice.all_notices.append(self)
	
	@classmethod
	def show_all_notices(self):
		index = 1
		for notice in self.all_notices:
			print(f"{index}.")
			print(notice.date)
			print(notice.title)
			print(notice.description)
			print("***********************")
			index += 1
		
	@classmethod
	def choose_notice(self, notice_type_array):
		index = 1
		if len(notice_type_array) < 1:
			print("There are currently no notices of this type.")
			print("***********************")
			return
		for notice in notice_type_array:
			print(f"{index}.")
			print(notice.date)
			print(notice.title)
			print(notice.description)
			print("***********************")
			index += 1
				