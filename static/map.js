$(function () {
    var mymap = L.map('mapid').setView([-34.53995, -58.695757167], 26);
    var latlngs = new Array();

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mymap);

    $.ajax({
        type: "DELETE",
        url: "api/locations"
    }
    ).done(function () {
        $.post({
            url: "api/locations",
            data: JSON.stringify({
                "usuario": "test",
                "posiciones": "$GPRMC,133603.00,A,3432.39702,S,05841.74543,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39710,S,05841.74549,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39715,S,05841.74552,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39719,S,05841.74558,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39722,S,05841.74561,W,0.323,,170519,,,A*72\n"
            }),
            dataType: "json",
            contentType: "application/json"
        }
        ).done(function () {
            console.log("Posiciones almacenadas satisfactoriamente.");

            $.get("api/locations").done(function (muestras) {

                for (i = 0; i < muestras.length - 1; i++) {
                    var posicion = muestras[i].posicion;
                    var latlng = [];
                    latlng[0] = parseFloat(posicion.latitud);
                    latlng[1] = parseFloat(posicion.longitud);
                    latlngs.push(latlng);
                    console.log(latlng);
                }
                
                L.polyline(latlngs, {color: 'blue'}).addTo(mymap);

            }).fail(function (mensaje) {
                console.log("Error al obtener posiciones.");
                console.log(mensaje.responseText);
            });

        }).fail(function (mensaje) {
            console.log("Error al almacenar posiciones.");
            console.log(mensaje.responseText);
        });
    })

});