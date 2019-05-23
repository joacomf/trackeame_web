$(function () {
    var mapa = new Mapa(-34.53995, -58.695757167);
    var parser = new Parser();

    $.ajax({
        type: "DELETE",
        url: "api/locations"
    }
    ).done(function () {
        $.post({
            url: "api/locations",
            data: JSON.stringify({
                "usuario": "test",
                "posiciones": "$GPRMC,133603.00,A,3432.39702,S,05841.74543,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3832.39710,S,05841.74549,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39715,S,05841.74552,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39719,S,05841.74558,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39722,S,05841.74561,W,0.323,,170519,,,A*72\n"
            }),
            dataType: "json",
            contentType: "application/json"
        }
        ).done(function () {
            console.log("Posiciones almacenadas satisfactoriamente.");

            $.get("api/locations").done(function (posiciones) {
                var posicionesParseadas = parser.parsearPosiciones(posiciones);
                mapa.marcarPosiciones(posicionesParseadas);
                mapa.dibujarMarcas();
                
            }).fail(function (mensaje) {
                console.log("Error al obtener posiciones.");
                console.log(mensaje.responseText);
            });

        }).fail(function (mensaje) {
            console.log("Error al almacenar posiciones.");
            console.log(mensaje.responseText);
        });
    }).fail(function (mensaje) {
        console.log("Error al eliminar posiciones.");
        console.log(mensaje.responseText);
    });;
});