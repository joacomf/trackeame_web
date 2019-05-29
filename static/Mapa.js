function Mapa(latitudInicial, longitudInicial) {
    var mapa = L.map('mapid').setView([latitudInicial, longitudInicial], 26);
    var posicionesMarcadas = [];

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mapa);

    /**
     * posiciones debe ser una lista de pares ordenados (latitud, longitud), donde
     * tanto latitud como longitud deben ser flotantes.
     */
    this.marcarPosiciones = function (posiciones) {

        for (i = 0; i < posiciones.length; i++) {
            var posicion = posiciones[i];
            posicionesMarcadas.push(posicion);
        }
    }

    this.dibujarMarcas = function () {
        L.polyline(posicionesMarcadas, {color: 'blue'}).addTo(mapa);
        mapa.panTo(posicionesMarcadas[0]);
    }
}