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

    locationsToAdd = [];
    
    // To draw the track
    // https://stackoverflow.com/questions/31305497/how-to-draw-an-arrow-on-every-polyline-segment-on-google-maps-v3
    flightPath = new google.maps.Polyline({
       path: locationsToAdd
       ,geodesic: true
       ,strokeColor: '#FF000'
       ,strokeOpacity: 0.6
       ,strokeWeight: 4
       ,icons: [{
           icon: {path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW}
           ,offset: '100%'
           ,repeat: '200px'
        }]
    });

    flightPath.setMap(map);

    // Center the map taking into account every position
    bounds = new google.maps.LatLngBounds();
}

function initMarkers(track) {
    track["cities_to_visit"].forEach(function (location) {
        let locationToAdd = {
            lat: parseFloat(location.lat)
            ,lng: parseFloat(location.lng)
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
    return new google.maps.Marker({
       position: locationToAdd
       ,map: map
    });
}