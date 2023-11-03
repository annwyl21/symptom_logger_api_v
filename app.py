from flask import Flask, request, jsonify
from FormatData import FormatData
from Visualize import Visualize

app = Flask(__name__)

@app.route('/slvapi/visualize', methods=['GET','POST'])
def visualize():
	if request.method == 'POST':
		data = request.json

		dates = FormatData.organize_date_data(data)
		times = FormatData.organize_time_data(data)
		pain = FormatData.organize_pain_data(data)
			
		scatterplot = Visualize.scatterplot(dates, times)
		bubbleplot = Visualize.bubbleplot(dates, times, pain)
		
		return jsonify({"scatterplot": scatterplot, "bubbleplot": bubbleplot})
	
	else:
		return jsonify({"error": "No data to summarize"})

if __name__ == '__main__':
	app.run(debug=True)
	#app.run()