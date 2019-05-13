import json
import unittest

class LocalizacionSteps(unittest.TestCase):

    contenido = None
    status = None
    response = None

    def cuando_guardo_en(self, ruta='', datos={}):
        print("Envio petición por POST con datos:", datos)
        self.response = self.app.post(ruta,
                                      data=json.dumps(datos),
                                      content_type='application/json')

        return self

    def entonces_corroboro_que_el_status_es_BAD_REQUEST(self):
        print("Tengo código de respuesta BAD REQUEST (403)")
        self.assertEqual(403, self.response.status_code)

    def limpiar_escenarios(self):
        self.contenido = None
        self.status = None
        self.response = None