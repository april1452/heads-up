from flask import Flask, render_template, request, json
from get_data import *
from get_csv import *

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
	return render_template('map.html')

@app.route('/loc')
def get_location():
	city = request.args.get('city')
	involving = request.args.get('inv')
	lat_lngs = get_lat_lng(city + '_' + involving + '.csv')
	return json.dumps(lat_lngs)

if __name__ == "__main__":
  app.run(debug=True)