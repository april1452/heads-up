from sodapy import Socrata
import csv
import sys

client = Socrata('data.cityofnewyork.us', 'XQsi9HUe9Ij5CQj1KF0gvwRw7', username='april_tran@brown.edu', password='!0Walruses')
MAX_LIMIT = 10000

def shutdown():
	client.close()

def write_to_csv(filename, data, injured, killed):
	with open(filename, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['time', 'lat', 'lng', 'injured', 'killed'])
		for row in data:
			writer.writerow([row['time'], row['latitude'], row['longitude'], row[injured], row[killed]])

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
	write_to_csv('manhattan_cycl.csv', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')

def get_manhattan_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='MANHATTAN' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('manhattan_ped.csv', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')

def get_brooklyn_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='BROOKLYN' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('brooklyn_cycl.csv', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')

def get_brooklyn_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='BROOKLYN' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('brooklyn_ped.csv', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')

def get_queens_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='QUEENS' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('queens_cycl.csv', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')

def get_queens_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='QUEENS' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('queens_ped.csv', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')

def get_bronx_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='BRONX' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('bronx_cycl.csv', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')

def get_bronx_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='BRONX' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('bronx_ped.csv', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')

def get_staten_island_cycl_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='STATEN ISLAND' AND (number_of_cyclist_injured>0 OR number_of_cyclist_killed>0)")
	write_to_csv('staten_island_cycl.csv', data, 'number_of_cyclist_injured', 'number_of_cyclist_killed')

def get_staten_island_ped_data():
	data = client.get("/resource/h9gi-nx95.json",
		limit=MAX_LIMIT,
		select="time,latitude,longitude,number_of_pedestrians_injured,number_of_pedestrians_killed,number_of_cyclist_injured,number_of_cyclist_killed",
		where="borough='STATEN ISLAND' AND (number_of_pedestrians_injured>0 OR number_of_pedestrians_killed>0)")
	write_to_csv('staten_island_ped.csv', data, 'number_of_pedestrians_injured', 'number_of_pedestrians_killed')