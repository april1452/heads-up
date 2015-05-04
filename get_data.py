from geojson import Point, Feature, FeatureCollection
from sodapy import Socrata
import csv
import geojson
import get_csv
import sys

client = Socrata('data.cityofnewyork.us', 'XQsi9HUe9Ij5CQj1KF0gvwRw7', username='april_tran@brown.edu', password='!0Walruses')
MAX_LIMIT = 10000

def shutdown():
	client.close()

def write_to_csv(filename, data, injured, killed):
	with open('static/csv/' + filename + '.csv', 'wb') as csvfile:
		writerCSV = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writerCSV.writerow(['time', 'lat', 'lng', 'injured', 'killed'])
		for row in data:
			writerCSV.writerow([row['time'], row['latitude'], row['longitude'], row[injured], row[killed]])

def write_to_geojson(borough, collision_type):
	filename = borough + '_' + collision_type
	collision_dict = get_csv.csv_to_dict(filename + '.csv')
	collisions = []
	for c in collision_dict:
		location = Point((c['lng'], c['lat']))
		collision = Feature(geometry=location, properties={'type':collision_type, 'borough':borough, 'injured':c['injured'], 'killed':c['killed']})
		collisions.append(collision)

	fc = FeatureCollection(collisions)
	with open('static/json/' + filename + '.json', 'w') as jsonfile:
		geojson.dump(fc, jsonfile)


def update():
	get_manhattan_cycl_data()
	get_manhattan_ped_data()
	get_brooklyn_cycl_data()
	get_brooklyn_ped_data()
	get_queens_cycl_data()
	get_queens_ped_data()
	get_bronx_cycl_data()
	get_bronx_ped_data()
	get_staten_island_cycl_data()
	get_staten_island_ped_data()
	shutdown()

def get_manhattan_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='MANHATTAN' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('manhattan_cycl', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')
	write_to_geojson('manhattan', 'cycl')

def get_manhattan_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='MANHATTAN' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('manhattan_ped', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')
	write_to_geojson('manhattan', 'ped')

def get_brooklyn_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='BROOKLYN' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('brooklyn_cycl', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')
	write_to_geojson('brooklyn', 'cycl')

def get_brooklyn_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='BROOKLYN' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('brooklyn_ped', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')
	write_to_geojson('brooklyn', 'ped')

def get_queens_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='QUEENS' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('queens_cycl', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')
	write_to_geojson('queens', 'cycl')

def get_queens_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='QUEENS' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('queens_ped', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')
	write_to_geojson('queens', 'ped')

def get_bronx_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='BRONX' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('bronx_cycl', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')
	write_to_geojson('bronx', 'cycl')

def get_bronx_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='BRONX' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('bronx_ped', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')
	write_to_geojson('bronx', 'ped')

def get_staten_island_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='STATEN ISLAND' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('staten_island_cycl', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')
	write_to_geojson('staten_island', 'cycl')

def get_staten_island_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='STATEN ISLAND' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('staten_island_ped', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')
	write_to_geojson('staten_island', 'ped')
