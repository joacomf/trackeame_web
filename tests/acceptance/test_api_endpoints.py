from server import init

import unittest
import json


class TrackeameAPIEndpointsTests(unittest.TestCase):

    database_url = 'mongodb://localhost:27017/test'
    database_name = 'test'

    @classmethod
    def setUpClass(self):
        # creates a test client
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

    def test_si_voy_a_obtener_usuario_obtengo_reponse_OK(self):
        # sends HTTP GET request to the application
        # on the specified path

        result = self.app.get('/api/users')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_si_voy_a_obtener_usuario_obtengo_al_usuario_JOAN_guardado_previamente(self):

        self.database.users.insert_one({"name": "JOAN", "lastname": "LALLA", "sex": 'M'})

        response = self.app.get('/api/users').get_data(as_text=True)

        result = json.loads(response)

        self.assertEqual('JOAN', result[0]['name'])
