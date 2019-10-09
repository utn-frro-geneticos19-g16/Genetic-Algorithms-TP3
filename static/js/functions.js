// Stats of the Track
function logTrack(track) {
    console.log("Stats Loading...");
    document.getElementById("sideStats").innerHTML = "<p>" + "BEST ROUTE STATS:" + "</p>" + "<br />";
    document.getElementById("sideStats").innerHTML += "<p style='padding-bottom: 10px'>" +
        "Total Distance: " +  track["accumulated_distance"] + " km" + "</p>" + "<hr />" + "<br />";
    track["cities_to_visit"].forEach(function (item) {
        document.getElementById("sideStats").innerHTML += "<p>" + item.name + ": " +
        item.lat + " | " + item.lng + "</p>" + "<br />";
        console.log(item.name, item.lat, item.lng);
    });
    document.getElementById("sideStats").innerHTML += "<hr />";
    document.getElementById("sideStats").innerHTML += "<div id='goBack' style='padding-top: 10px'>" +
        "<a>" + "\u21a9 Back to Index" + "</a>" + "</div>" + "<br />";
    console.log("Total Distance: " + track["accumulated_distance"] + " km");
    console.log("Fully Loaded!");
}

// Get the Modal
let modal = document.getElementById("overlayModal");

// Get the Button that opens the Modal
let btn = document.getElementById("opt1");

// Get the <span> element that closes the Modal
let closeSpan = document.getElementsByClassName("close")[0];

// When the user clicks on the Button, open the Modal
btn.onclick = function() {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the Modal
closeSpan.onclick = function() {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the Modal, close it
window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = "none";
  }
};

// Root URL
let urlRoot = "http://127.0.0.1:5000/";

// URI with Map Endpoint
let uriMap = urlRoot + "Map/";

// Run! inside-modal button
let runBtn = document.getElementById("citySend");

// Reload Page (Exercise 2-A)
runBtn.onclick = function() {
    // City name
    let cityName = document.getElementById("cityName").value;
    window.location.href = uriMap + cityName;
};

// "Go Back" Button
let backBtn = document.getElementById("goBack");

// Back to Index (Doesn't Work, Bubbling problem!)
backBtn.addEventListener('click', function (e) {
    // backBtn.onclick = function() { window.location.href = urlRoot; };
   e.preventDefault();
   window.location.href = urlRoot;
}, true);
