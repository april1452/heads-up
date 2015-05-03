from pandas import *
from numpy import *

def csv_to_dict(filename):
	csv_data = pandas.io.parsers.read_csv(filename, quotechar='"')
	dict_data = []
	for row in csv_data.values:
		dict_data.append({'time':row[0], 'lat':row[1], 'lng':row[2], 'injured':row[3], 'killed':row[4]})
	return dict_data

def get_lat_lng(filename):
	csv_data = pandas.io.parsers.read_csv(filename, quotechar='"')
	dict_data = []
	for row in csv_data.values:
		dict_data.append({'lat':row[1], 'lng':row[2]})
	return dict_data