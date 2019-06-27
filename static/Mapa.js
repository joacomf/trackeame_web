function Mapa(latitudInicial, longitudInicial) {
    var mapa = L.map('mapid').setView([latitudInicial, longitudInicial], 26);
    var posicionesMarcadas = [];
    var paradasMarcadas = [];

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mapa);

    /**
     * posiciones debe ser una lista de ternas ordenadas (latitud, longitud, esParada),
     * donde tanto latitud como longitud deben ser flotantes y esParada debe ser booleano.
     */
    this.marcarPosiciones = function (posiciones) {

        for (i = 0; i < posiciones.length; i++) {
            var posicion = posiciones[i];
            var parLatitudLongitud = posicion.slice(0, 2);
            var posicionEsParada = posicion[2];

            if (posicionEsParada) {
                paradasMarcadas.push(parLatitudLongitud);
            } else {
                posicionesMarcadas.push(parLatitudLongitud);
            }
        }
    }

    this.dibujarMarcas = function () {

        for (i = 0; i < paradasMarcadas.length; i++) {
            var parada = paradasMarcadas[i];
            L.marker(parada).addTo(mapa);
            mapa.panTo(parada);
        }

        L.polyline(posicionesMarcadas, {color: 'blue'}).addTo(mapa);
        mapa.panTo(posicionesMarcadas[0]);
    }
}