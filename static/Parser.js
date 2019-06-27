function Parser() {

    this.parsearPosiciones = function (posiciones) {
        var posicionesParseadas = [];

        for (i = 0; i < posiciones.length; i++) {
            var posicion = posiciones[i].posicion;
            latitud = parseFloat(posicion.latitud);
            longitud = parseFloat(posicion.longitud);
            tiempoDeParada = parseFloat(posicion.tiempoDeParada);
            posicionParseada = new Posicion(latitud, longitud, tiempoDeParada);
            posicionesParseadas.push(posicionParseada);
        }

        return posicionesParseadas;
    }
}