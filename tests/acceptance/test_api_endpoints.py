from server import init

import unittest
import json


class TrackeameAPIEndpointsTests(unittest.TestCase):

    database_url = 'mongodb://localhost:27017/test'
    database_name = 'test'

    contenido = None
    status = None
    response = None

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

        self.contenido = None
        self.status = None
        self.response = None

    def test_si_voy_a_obtener_usuario_obtengo_status_OK(self):
        self.cuando_voy_a_('/api/users')

        self.entonces_corroboro_que_el_status_es_OK()

    def test_si_voy_a_obtener_usuario_obtengo_al_usuario_JOAN_guardado_previamente(self):
        joan = {"name": "JOAN", "lastname": "LALLA", "sex": 'M'}

        self.dado_el_usuario_(joan)

        self.cuando_voy_a_('/api/users').obtengo_lista_de_usuarios()

        self.entonces_corroboro_que_el_unico_usuario_es_(joan)

    def cuando_voy_a_(self, ruta=''):
        self.response = self.app.get(ruta)

        return self

    def obtengo_contenido(self):
        return self.response.get_data(as_text=True)

    def obtengo_lista_de_usuarios(self):
        self.contenido = json.loads(self.obtengo_contenido())

        return self

    def dado_el_usuario_(self, usuario):
        self.database.users.insert_one(usuario)

    def entonces_corroboro_que_el_unico_usuario_es_(self, usuario):
        self.assertEqual(usuario['name'], self.contenido[0]['name'])
        self.assertEqual(usuario['lastname'], self.contenido[0]['lastname'])

    def entonces_corroboro_que_el_status_es_OK(self):
        self.assertEqual(200, self.response.status_code)