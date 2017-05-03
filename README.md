# headsUp

Bicycle helmets are seen as so integral to cyclist safety that the state of New York has required by law that children under 14 wear helmets while riding their bikes. However, in NYC, the data shows that **more motor vehicle accidents occur involving pedestrians** rather than cyclists. If it's more dangerous to be a pedestrian, who should be wearing the helmets?

## Running

Make sure you have `virtualenv` installed. From the root folder:
```
source venv/bin/activate
python heads_up.py
# At this point you may see
# ImportError: No module named pandas
# which means you should run
pip install pandas
```
In your browser window, navigate to `localhost:5000`

## Features

See motor vehicle collisions in NYC that involved either pedestrians or cyclists from July 2012 to present. Examine collision distribution in all five boroughs, and see statistics from Manhattan's neighborhoods.

![Screenshot](https://github.com/phucanhapril/heads-up/raw/master/static/bikes.png "Screenshot")

## Proprietary

Phuc Anh (April) Tran. Developed for Christian Swinehart's *Lies, Damned Lies, and Dataviz* course at Rhode Island School of Design, Spring 2015. Data from NYCOpenData.

## TODO

* Neighborhood statistics
* Find way to remove unneeded geojson from data layer
* Needs cronjob for updating data automatically
* Markers should enlarge with window zoom
