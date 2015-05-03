var map;
var collision;

$(document).ready(function() {
	initialize();
  // Get and map initial collision points for ped/cycl in Manhattan
 //  setTimeout(function(){
 //    drawManhattanPed();
	// }, 1000);
});

function initialize() {
	 var styles = [
	  {
	    featureType: "all",
	    stylers: [{lightness: 10},{saturation: -90}]
	  },{
	  	featureType: "poi",
    	elementType: "labels",
    	stylers: [{visibility: "off"}]
	  },{
	  	featureType: "transit",
    	elementType: "labels",
    	stylers: [{visibility: "off"}]
	  },{
	  	featureType: "road",
    	elementType: "labels.icon",
    	stylers: [{visibility: "off"}]
	  }
	];
	var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});

  var mapOptions = {
    zoom: 13,
    center: new google.maps.LatLng(40.749, -73.95), // Manhattan
    mapTypeControlOptions: {mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']}
  };

  // Create map and add styled map
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  map.mapTypes.set('map_style', styledMap);
  map.setMapTypeId('map_style');
}

function drawCollision(color, lat, lng) {
	var collisionOptions = {
    strokeColor: color,
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: color,
    fillOpacity: 0.35,
    map: map,
    center: new google.maps.LatLng(lat, lng),
    radius: 10
	};

	// Add a point for each collision to the map
	collision = new google.maps.Circle(collisionOptions);
}

function getAndDraw(cityName, involving) {
	var color = '';
	if (involving == 'ped')
		color = '#7f0f7e';
	else color = '#fec0cb';

	$.getJSON("/loc", {city: cityName, inv: involving})
  	.done(function(json) {
    	for (var j in json) {
        drawCollision(color, json[j].lat, json[j].lng);
    	}
  });
}

/** DRAWING FUNCTIONS ********************************************************/
function drawManhattanPed() {
	getAndDraw('manhattan', 'ped');
}

function drawManhattanCycl() {
	getAndDraw('manhattan', 'cycl');
}

function drawBrooklynPed() {
	getAndDraw('brooklyn', 'ped');
}

function drawBrooklynCycl() {
	getAndDraw('brooklyn', 'cycl');
}

function drawQueensPed() {
	getAndDraw('queens', 'ped');
}

function drawQueensCycl() {
	getAndDraw('queens', 'ped');
}

function drawBronxPed() {
	getAndDraw('bronx', 'ped');
}

function drawBronxCycl() {
	getAndDraw('bronx', 'ped');
}

function drawStatenIslandPed() {
	getAndDraw('staten_island', 'ped');
}

function drawStatenIslandCycl() {
	getAndDraw('staten_island', 'ped');
}
