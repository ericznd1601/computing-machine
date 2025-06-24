const map = L.map('map').setView([-15.7942, -47.8822], 4);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

map.on('click', function(e) {
    const lat = e.latlng.lat;
    const lon = e.latlng.lng;

    fetch('/api/check', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({lat, lon})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('result').textContent =
            `Tipo de estrada: ${data.surface}`;
        document.getElementById('json-output').textContent =
            JSON.stringify(data, null, 2);
    });
});
