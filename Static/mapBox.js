mapboxgl.accessToken = 'pk.eyJ1Ijoib2E3ODUiLCJhIjoiY2x0NW9vOWNkMDJsYjJpbW1qYms4aDRvdiJ9.FTsvDp3pQmcWOw_axFcsGA';
let kilometers;
let miles;
navigator.geolocation.getCurrentPosition(successLocation, errorLocation,
    {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
    })

function successLocation(position) {
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    map.flyTo({
        center: [lng, lat],
        zoom: 15
    });
}

function errorLocation(error) {
    console.warn(`ERROR(${error.code}): ${error.message}`);
}

const map = new mapboxgl.Map({
    container: 'map', // container ID
    style: 'mapbox://styles/mapbox/streets-v12', // style URL
    center: [-74.5, 40], // starting position [lng, lat]
    zoom: 9, // starting zoom
});

map.addControl(new mapboxgl.NavigationControl());


var directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken

});

map.addControl(directions, 'top-left');
// Event listener for route updates
directions.on('route', function (e) {
    if (e.route && e.route[0] && e.route[0].distance) {
        // Extract distance information
        const distanceInMeters = e.route[0].distance;

        // Convert meters to kilometers or miles as needed
        const distanceInKilometers = distanceInMeters / 1000;
        const distanceInMiles = distanceInMeters / 1609.34;

        // Log or send the distance to the backend
        console.log('Distance in kilometers:', distanceInKilometers);
        console.log('Distance in miles:', distanceInMiles);
        kilometers=distanceInKilometers;
        miles=distanceInMiles;

    }
});

//----------------------------------------------------
function sendDistanceToFlask(kilometers, miles) {
    // Prepare the form data
    const formData = new URLSearchParams();
    formData.append('kilometers', kilometers);
    formData.append('miles', miles);
    console.log(formData)
    // Make an AJAX request to Flask route
    fetch('http://localhost:5000/journy_pricing', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({'distanceInKilometers': kilometers, 'distanceInMiles': miles}),
        }
    ).then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


function calculatePrice() {
    // Your existing code to calculate the price...

    // Get the form data
    const pickupPoint = document.getElementById('pickupPoint').value;
    const landingPoint = document.getElementById('landingPoint').value;

    // Additional logic to calculate the price or perform other actions...
    if ( kilometers && miles ){
    // Send the distance data to Flask server
    sendDistanceToFlask(kilometers, miles);
    }
}

