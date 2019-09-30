function showTrack(track) {
    track["cities_to_visit"].forEach(function (item) {
        document.writeln(item.name + ": "
            + item.lat + "-" + item.long + "\n");
        console.log(item.name, item.lat, item.long);
    });

    document.writeln("Total Distance = " + track["accumulated_distance"] + "\n");
    console.log(track["accumulated_distance"]);
}
