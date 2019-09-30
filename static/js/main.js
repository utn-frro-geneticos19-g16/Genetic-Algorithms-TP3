function sendCities(cities) {
    cities.forEach(function (item) {
        document.writeln(item.name + ": "
            + item.lat + "-" + item.long);
        console.log(item.name, item.lat, item.long);
    })
}
