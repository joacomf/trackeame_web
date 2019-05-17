import json
import unittest

class LocalizacionSteps(unittest.TestCase):

    contenido = None
    status = None
    response = None

    def cuando_voy_a_(self, ruta=''):
        self.response = self.app.get(ruta)
        return self

    def cuando_guardo_en(self, ruta='', datos={}):
        print("Envio petición por POST con datos:", datos)
        self.response = self.app.post(ruta,
                                      data=json.dumps(datos),
                                      content_type='application/json')

        return self

    def entonces_corroboro_que_el_status_es_BAD_REQUEST(self):
        print("Tengo código de respuesta BAD REQUEST (403)")
        self.assertEqual(403, self.response.status_code)

    def obtengo_contenido(self):
        return self.response.get_data(as_text=True)

    def obtengo_lista_de_posiciones(self):
        print("Obtengo lista de posiciones desde el body del response")
        self.contenido = json.loads(self.obtengo_contenido())
        print(self.contenido)
        return self

    def entonces_corroboro_que_las_posiciones_son(self, posiciones):
        print("Corroboro que las posiciones es", posiciones[0]['posicion'])
        self.assertEqual(posiciones[0]['posicion']['latitud'], self.contenido[0]['posicion']['latitud'])
        self.assertEqual(posiciones[0]['posicion']['longitud'], self.contenido[0]['posicion']['longitud'])


    def limpiar_escenarios(self):
        self.contenido = None
        self.status = None
        self.response = None