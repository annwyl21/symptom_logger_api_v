import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker

# UUID - Update this to give each image a unique identifier so the URL sent back to the user is unique

class Visualize():
	
	def scatterplot(dates, times):
		plt.switch_backend('Agg') # this changes where the computer generates the chart because that caused a problem on the Mac but not on windows

		plt.figure(figsize=(4, 3))
		ax=plt.subplot()
		plt.subplots_adjust(bottom = 0.2, left = 0.2)

		plt.scatter(dates, times, marker='x', color='#5e747f', s=40)

		ax.set_yticks([0, 4, 8, 12, 16, 20, 24]) # This sets the y-axis to show every 4 hours
		
		plt.xticks(fontsize=6, rotation=45)
		plt.xlabel('Date', fontsize=8)
		plt.ylabel('Time of Day', fontsize=8)
		plt.title('My Symptom Record')
		
		plt.savefig('static/images/scatterplot.png', transparent=True)
		#plt.show()
		return "https://visualizesl.onrender.com/static/images/scatterplot.png"
	
	def bubbleplot(dates, times, pain):
		# Square the 'pain' values to make the size differences more distinct for the simple 1-10 pain scale
		scaled_pain = [p**2 for p in pain]

		plt.switch_backend('Agg') # this changes where the computer generates the chart because that caused a problem on the Mac but not on windows

		plt.figure(figsize=(4, 3))
		ax=plt.subplot()
		plt.subplots_adjust(bottom = 0.2, left = 0.2)
		plt.scatter(dates, times, s=scaled_pain, alpha=0.5, color='#5e747f')

		ax.set_yticks([0, 4, 8, 12, 16, 20, 24])
		# ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) 
		# ax.yaxis.set_major_locator(ticker.MultipleLocator(4))

		plt.xticks(fontsize=6, rotation=45)
		plt.xlabel('Date', fontsize=8)
		plt.ylabel('Time of Day', fontsize=8, )
		plt.title('My Symptom Record')
		plt.savefig('static/images/bubbleplot.png', transparent=True)
		# plt.show()
		return "https://visualizesl.onrender.com/static/images/bubbleplot.png"
