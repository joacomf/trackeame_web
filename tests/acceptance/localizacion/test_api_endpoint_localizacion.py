from server import init
from .localizacion_steps import LocalizacionSteps

class LocalizacionAceptacionTest(LocalizacionSteps):

    database_url = 'mongodb://localhost:27017/test'
    database_name = 'test'

    @classmethod
    def setUpClass(self):
        app = init(self.database_url, self.database_name)

        self.mongo = app.mongo
        self.database = app.database

        self.app = app.test_client()
        self.app.testing = True

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.mongo.drop_database('test')

        self.limpiar_escenarios()

    def test_si_voy_a_guardar_localizaciones_con_5_localizaciones_se_guardan_correctamente(self):
        json = {
                "usuario": "test",
                "posiciones": "$GPRMC,133603.00,A,3432.39702,S,05841.74543,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39710,S,05841.74549,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39715,S,05841.74552,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39719,S,05841.74558,W,0.323,,170519,,,A*72\n$GPRMC,133603.00,A,3432.39722,S,05841.74561,W,0.323,,170519,,,A*72\n"
                }

        self.cuando_guardo_en('/api/locations', json)

        self.cuando_voy_a_('/api/locations').obtengo_lista_de_posiciones()

        respuesta_esperada = [{'posicion': {'latitud': -34.53995, 'longitud': -58.69575666666667, 'esParada': False}},
                              {'posicion': {'latitud': -34.53995166666667, 'longitud': -58.69575666666667, 'esParada': False}},
                              {'posicion': {'latitud': -34.53995166666667, 'longitud': -58.69575833333333, 'esParada': False}},
                              {'posicion': {'latitud': -34.53995166666667, 'longitud': -58.69575833333333, 'esParada': False}},
                              {'posicion': {'latitud': -34.53995333333334, 'longitud': -58.69576, 'esParada': False}}]

        self.entonces_corroboro_que_las_posiciones_son(respuesta_esperada)

    def test_si_voy_a_guardar_localizaciones_con_formato_erroneo_obtengo_403(self):
        self.cuando_guardo_en('/api/locations', {"clave_invalida": "Hola\nComo\nEstas?"})

        self.entonces_corroboro_que_el_status_es_BAD_REQUEST()

    def test_si_almaceno_una_parada_en_una_posicion_se_almacena_correctamente(self):
        json_de_posiciones_con_parada = {
            "usuario": "test",
            "posiciones": "$GPRMC,133603.00,A,3432.39702,S,05841.74543,W,0.323,,170519,,,A*72\n" +
                          "$PARADA,133603.00,A,3432.39702,S,05841.74543,W,0.323,,170519,,,A*72\n"
        }
        self.cuando_guardo_en('/api/locations', json_de_posiciones_con_parada)
        self.cuando_voy_a_('/api/locations').obtengo_lista_de_posiciones()

        respuesta_esperada = [{'posicion': {'latitud': -34.53995, 'longitud': -58.69575666666667, 'esParada': False}},
                              {'posicion': {'latitud': -34.53995, 'longitud': -58.69575666666667, 'esParada': True}}]

        self.entonces_corroboro_que_las_posiciones_son(respuesta_esperada)
