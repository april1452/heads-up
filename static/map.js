var map;
function initialize() {
  var mapOptions = {
    zoom: 13,
    center: new google.maps.LatLng(40.749, -73.97)
  };

  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);