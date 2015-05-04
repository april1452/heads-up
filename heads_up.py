from flask import Flask, render_template, request, json
import get_data


app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
	# get_data.update()
	return render_template('map.html')

if __name__ == "__main__":
  app.run(debug=True)