function initMap() {
    // Central reference location, UTN FRRo
    baseLocation = {lat: -32.95476, lng: -60.6459824};
    // Map, hiding business and other unnecessary stuff
    map = new google.maps.Map(
        document.getElementById('map'), {
            center: baseLocation
            ,zoom: 15
            ,styles: [{"featureType": "poi.business","stylers": [{ "visibility": "off" }]}]
            ,mapTypeControl: false
            ,fullscreenControl: false
            ,streetViewControl: false
        });

    var flightPlanCoordinates = [
          {lat: 37.772, lng: -122.214},
          {lat: 21.291, lng: -157.821},
          {lat: -18.142, lng: 178.431},
          {lat: -27.467, lng: 153.027}
        ];


    // To draw the track
    flightPath = new google.maps.Polyline({
       path: flightPlanCoordinates
       ,geodesic: true
       ,strokeColor: '#FF000'
       ,strokeOpacity: 0.6
       ,strokeWeight: 4
    });

    flightPath.setMap(map);

    // Center the map taking into account every position
    bounds = new google.maps.LatLngBounds();
}

function initMarkers(track) {
    let locationsToAdd = [];

    track["cities_to_visit"].forEach(function (location) {
        let locationToAdd = {
            lat: parseFloat(location.lat)
            ,lng: parseFloat(location.long)
        };

        console.log(locationToAdd);

        locationsToAdd.push(locationToAdd);
    });

    locationsToAdd.forEach(function (location) {
        console.log(location.lat, location.lng);
    });

    flightPath.setPath(locationsToAdd);

    console.log(flightPath);
}

function newMarker(locationToAdd) {
    let marker = new google.maps.Marker({
       position: locationToAdd
       ,map: map
    });

    return marker;
}