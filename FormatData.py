from datetime import datetime

class FormatData:

	def organize_date_data(data):
		dates = []
		for i in range(len(data)):
			new_date = data[i]["date"]
			date = FormatData.us_to_uk_date_format(new_date)
			dates.append(date)
		return dates

	def us_to_uk_date_format(date):
		date_time_format = datetime.strptime(str(date), '%Y-%m-%d')
		#uk_date = date_time_format.strftime('%d %B %Y') # returns uk date format
		uk_date = date_time_format.strftime('%d-%b') # returns d/m format
		return uk_date
	
	def organize_time_data(data):
		times = []
		for i in range(len(data)):
			new_time = data[i]["time"]
			time = FormatData.remove_seconds_notation(new_time)
			times.append(time)
		return times

	def remove_seconds_notation(time):
		time = str(time)
		time = time[:-3]
		return time
	
	def remove_minutes_notation(time):
		time = str(time)
		time = time[:-6]
		return time

	def organize_pain_data(data):
		pain = []
		for i in range(len(data)):
			new_pain = data[i]["pain_score"]
			pain.append(new_pain)
		return pain
	
