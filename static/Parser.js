function Parser() {

    this.parsearPosiciones = function (posiciones) {
        var posicionesParseadas = [];

        for (i = 0; i < posiciones.length; i++) {
            var posicion = posiciones[i].posicion;
            var latlng = [];
            latlng[0] = parseFloat(posicion.latitud);
            latlng[1] = parseFloat(posicion.longitud);
            posicionesParseadas.push(latlng);
        }

        return posicionesParseadas;
    }
}