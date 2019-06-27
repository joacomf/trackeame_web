function Parser() {

    this.parsearPosiciones = function (posiciones) {
        var posicionesParseadas = [];

        for (i = 0; i < posiciones.length; i++) {
            var posicion = posiciones[i].posicion;
            var posicionParseada = [];
            posicionParseada[0] = parseFloat(posicion.latitud);
            posicionParseada[1] = parseFloat(posicion.longitud);
            posicionParseada[2] = posicion.esParada;
            posicionesParseadas.push(posicionParseada);
        }

        return posicionesParseadas;
    }
}