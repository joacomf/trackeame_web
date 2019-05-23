$(function () {
    var mapa = new Mapa(-34.53995, -58.695757167);
    var parser = new Parser();

    $.get("api/locations").done(function (posiciones) {
        var posicionesParseadas = parser.parsearPosiciones(posiciones);
        mapa.marcarPosiciones(posicionesParseadas);
        mapa.dibujarMarcas();
        
    }).fail(function (mensaje) {
        console.log("Error al obtener posiciones.");
        console.log(mensaje.responseText);
    });
});