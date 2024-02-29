mapboxgl.accessToken = 'pk.eyJ1Ijoib2E3ODUiLCJhIjoiY2x0NW9vOWNkMDJsYjJpbW1qYms4aDRvdiJ9.FTsvDp3pQmcWOw_axFcsGA';

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
