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

    def test_si_voy_a_guardar_localizaciones_con_formato_erroneo_obtengo_403(self):
        self.cuando_guardo_en('/api/locations', {"clave_invalida": "Hola\nComo\nEstas?"})

        self.entonces_corroboro_que_el_status_es_BAD_REQUEST()

"""     def test_si_voy_a_obtener_usuario_obtengo_al_usuario_JOAN_guardado_previamente(self):
        joan = {"name": "JOAN", "lastname": "LALLA", "sex": 'M'}

        self.dado_el_usuario_(joan)

        self.cuando_voy_a_('/api/users').obtengo_lista_de_usuarios()

        self.entonces_corroboro_que_el_unico_usuario_es_(joan) """