function Posicion(latitud, longitud, tiempoDeParada) {
    var parLatitudLongitud = [latitud, longitud]
    var esParada = tiempoDeParada > 0;

    this.parLatitudLongitud = function () {
        return parLatitudLongitud;
    };

    this.esParada = function () {
        return esParada;
    };

    this.tiempoDeParada = function () {
        return tiempoDeParada;
    };
}