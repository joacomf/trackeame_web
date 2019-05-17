$(function () {
    var mymap = L.map('mapid').setView([-34.604878, -58.563051], 26);
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
                "posiciones": "-34.605851,-58.563338\n" +
                        "-34.605847,-58.563751\n" +
                        "-34.605473,-58.563864\n" +
                        "-34.605079,-58.563845\n" +
                        "-34.604997,-58.563850\n" +
                        "-34.604959,-58.563837\n" +
                        "-34.604880,-58.563710\n" +
                        "-34.604887,-58.563461\n" +
                        "-34.604878,-58.563051\n"
            }),
            dataType: "json",
            contentType: "application/json"
        }
        ).done(function () {
            console.log("Posiciones almacenadas satisfactoriamente.");

            $.get("api/locations").done(function (posiciones) {

                for (i = 0; i < posiciones.length - 1; i++) {
                    var posicion = posiciones[i].posicion;
                    posicion[0] = parseFloat(posicion[0]);
                    posicion[1] = parseFloat(posicion[1]);
                    latlngs.push(posicion);
                }
                
                var polyline = L.polyline(latlngs, {color: 'blue'}).addTo(mymap);

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