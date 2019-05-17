from server import init

import unittest
import json


class TrackeameFrontPageTests(unittest.TestCase):

    database_url = 'mongodb://localhost:27017/test'
    database_name = 'test'

    contenido = None
    status = None
    response = None

    @classmethod
    def setUpClass(self):
        app = init(self.database_url, self.database_name)

        self.app = app.test_client()
        self.app.testing = True

    @classmethod
    def tearDownClass(self):
        self.contenido = None
        self.status = None
        self.response = None

    def test_si_voy_a_la_pagina_principal_obtengo_200_y_nombre_de_la_aplicacion(self):

        self.cuando_voy_a_('/')

        self.entonces_corroboro_que_el_status_es_OK()
        self.y_que_se_ve_el_texto_("Trackeame")

    def cuando_voy_a_(self, ruta=''):
        self.response = self.app.get(ruta)

        return self

    def entonces_corroboro_que_el_status_es_OK(self):
        self.assertEqual(200, self.response.status_code)

    def obtengo_contenido(self):
        return self.response.get_data(as_text=True)

    def y_que_se_ve_el_texto_(self, texto):
        self.assertIn(texto, self.obtengo_contenido())