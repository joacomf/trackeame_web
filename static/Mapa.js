function Mapa(latitudInicial, longitudInicial) {
    var mapa = L.map('mapid').setView([latitudInicial, longitudInicial], 26);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mapa);

    /**
     * posiciones debe ser una lista de objetos de tipo Posicion.
     */
    this.dibujarMarcas = function (posiciones) {
        var paresLatitudLongitud = [];

        for (i = 0; i < posiciones.length; i++) {
            var posicion = posiciones[i];
            var parLatitudLongitud = posicion.parLatitudLongitud();
            
            if (posicion.esParada()) {
                var marca = L.marker(parLatitudLongitud);
                marca.bindPopup("Tiempo: " + posicion.tiempoDeParada() + " s");
                marca.addTo(mapa);
            }

            paresLatitudLongitud.push(parLatitudLongitud);
        }

        L.polyline(paresLatitudLongitud, {color: 'blue'}).addTo(mapa);
        mapa.panTo(paresLatitudLongitud[0]);
    }
}