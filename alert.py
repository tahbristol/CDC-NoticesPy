class Alert():
	alerts = []
	
	def __init__(self, description, readme_link):
		self.description = description
		self.readme_link = readme_link
	
	def save_alert(self):
		Alert.alerts.append(self)
		
	def all_alerts(self):
		return Alert.alerts
	
	def get_title(self):
		title = ''
		for word in link.split('/')[-1].split('-'):
			title += " " + word.capitalize()
		return title	