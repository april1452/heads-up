from flask import Flask, render_template, request, jsonify
import json
from data import *

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
	return render_template('map.html')

if __name__ == "__main__":
  app.run(debug=True)