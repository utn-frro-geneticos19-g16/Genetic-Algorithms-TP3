function logTrack(track) {
    console.log("Stats Loading...");
    document.getElementById("sideStats").innerHTML = "<p style='padding-bottom: 10px'>" +
        "BEST ROUTE STATS:" + "</p>" + "<hr />" + "<br />";
    track["cities_to_visit"].forEach(function (item) {
        document.getElementById("sideStats").innerHTML += "<p>" + item.name + ": " +
        item.lat + " | " + item.lng + "</p>" + "<br />";
        console.log(item.name, item.lat, item.lng);
    });
    document.getElementById("sideStats").innerHTML += "<hr />";
    document.getElementById("sideStats").innerHTML += "<p style='padding-top: 10px'>" + "Total Distance: " +
        track["accumulated_distance"] + " km" + "</p>" + "<br />";
    console.log("Total Distance: " + track["accumulated_distance"] + " km");
    console.log("Fully Loaded!");
}
