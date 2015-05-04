var map;
var collision;
var loaded = {'mc':false, 'bc':false, 'qc':false, 'bxc':false, 'sic':false, 'mp':false, 'bp':false, 'qp':false, 'bxp':false, 'sip':false};
var vis = {'mc':false, 'bc':false, 'qc':false, 'bxc':false, 'sic':false, 'mp':false, 'bp':false, 'qp':false, 'bxp':false, 'sip':false};

$(document).ready(function() {
	initialize();

  // Get and map initial collision points for ped/cycl in Manhattan
  setTimeout(function(){ 
		drawManhattanCycl();
  	drawManhattanPed();
  }, 800);

  loaded['mc'] = true;
  loaded['mp'] = true;
  vis['mc'] = true;
  vis['mp'] = true;
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
	  },{
	  	featureType: "road.highway",
    	elementType: "geometry",
    	stylers: [{lightness: 15}]
	  }
	];
	var styledMap = new google.maps.StyledMapType(styles, {name: "Styled Map"});

  var mapOptions = {
    zoom: 13,
    center: new google.maps.LatLng(40.749, -73.974), // Manhattan
    mapTypeControlOptions: {mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']}
  };

  // Create map and add styled map
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  map.mapTypes.set('map_style', styledMap);
  map.setMapTypeId('map_style');
}

/** TOGGLER LISTENERS ********************************************************/
// If toggle was checked, hide collisions now. If toggle was unchecked, show collisions
$('.aTog').click(function() {
	var wasChecked = $('#' + $(this).attr('id') + ' > span').hasClass('checked');
	if (wasChecked) {
		hideCollisions($(this).attr('borough'), $(this).attr('collision'));
	} else {
		showCollisions($(this).attr('borough'), $(this).attr('collision'));
	}
});

function showCollisions(borough, collisionType) {
	// Load points if not already loaded
	checkAndLoad(borough, collisionType);

	map.data.setStyle(function(feature) {
    var myBorough = feature.getProperty('borough');
    var myCollisionType = feature.getProperty('type');
    var iconPath = myCollisionType == 'cycl' ? '/ped-pt.png' : '/cycl-pt.png';

    var myVisibility;
    if (myBorough == borough && myCollisionType == collisionType) {
    	myVisibility = true;
    	vis[getIndex(myBorough, myCollisionType)] = true;
    } else {
    	myVisibility = vis[getIndex(myBorough, myCollisionType)];
    }
    return {
      visible: myVisibility,
      icon: iconPath
    };
	});
}

function hideCollisions(borough, collisionType) {
	map.data.setStyle(function(feature) {
    var myBorough = feature.getProperty('borough');
    var myCollisionType = feature.getProperty('type');
    var iconPath = myCollisionType == 'cycl' ? '/ped-pt.png' : '/cycl-pt.png';

    var myVisibility;
    if (myBorough == borough && myCollisionType == collisionType) {
    	myVisibility = false;
    	vis[getIndex(myBorough, myCollisionType)] = false;
    } else {
    	myVisibility = vis[getIndex(myBorough, myCollisionType)];
    }
    return {
      visible: myVisibility,
      icon: iconPath
    };
	});
}

function getIndex(borough, collisionType) {
	if (borough == 'brooklyn') {
		if (collisionType == 'cycl') {
			loadIndex = 'bc';
		} else {
			loadIndex = 'bp';
		}
	} else if (borough == 'queens') {
		if (collisionType == 'cycl') {
			loadIndex = 'qc';
		} else {
			loadIndex = 'qp';
		}
	} else if (borough == 'bronx') {
		if (collisionType == 'cycl') {
			loadIndex = 'bxc';
		} else {
			loadIndex = 'bxp';
		}
	} else if (borough == 'staten_island') {
		if (collisionType == 'cycl') {
			loadIndex = 'sic';
		} else {
			loadIndex = 'sip';
		}
	} else {
		if (collisionType == 'cycl') {
			loadIndex = 'mc';
		} else {
			loadIndex = 'mp';
		}
	}
	return loadIndex;
}

/** DRAWING FUNCTIONS ********************************************************/
function drawCollisions(borough, collisionType) {
	map.data.loadGeoJson('/json/' + borough + '_' + collisionType + '.json');

	map.data.setStyle(function(feature) {
    var collisionType = feature.getProperty('type');
    var iconPath = collisionType == 'cycl' ? '/ped-pt.png' : '/cycl-pt.png';
    return {
      icon: iconPath
    };
	});
}

function checkAndLoad(borough, collisionType) {
	var loadIndex = getIndex(borough, collisionType);
	if (loaded[loadIndex] == 0) {
		drawCollisions(borough, collisionType);
	}
}

function drawAll() {
	drawAllPed();
	drawAllCycl();
}

function drawAllPed() {
	drawManhattanPed();
	drawBrooklynPed();
	drawQueensPed();
	drawBronxPed();
	drawStatenIslandPed();
}

function drawAllCycl() {
	drawManhattanCycl();
	drawBrooklynCycl();
	drawQueensCycl();
	drawBronxCycl();
	drawStatenIslandCycl();
}

function drawManhattanPed() {
	drawCollisions('manhattan', 'ped');
}

function drawManhattanCycl() {
	drawCollisions('manhattan', 'cycl');
}

function drawBrooklynPed() {
	drawCollisions('brooklyn', 'ped');
}

function drawBrooklynCycl() {
	drawCollisions('brooklyn', 'cycl');
}

function drawQueensPed() {
	drawCollisions('queens', 'ped');
}

function drawQueensCycl() {
	drawCollisions('queens', 'cycl');
}

function drawBronxPed() {
	drawCollisions('bronx', 'ped');
}

function drawBronxCycl() {
	drawCollisions('bronx', 'cycl');
}

function drawStatenIslandPed() {
	drawCollisions('staten_island', 'ped');
}

function drawStatenIslandCycl() {
	drawCollisions('staten_island', 'cycl');
}
