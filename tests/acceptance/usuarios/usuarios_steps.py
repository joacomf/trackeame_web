import json
import unittest

class UsuariosSteps(unittest.TestCase):

    contenido = None
    status = None
    response = None

    def cuando_voy_a_(self, ruta=''):
        self.response = self.app.get(ruta)
        return self

    def obtengo_contenido(self):
        return self.response.get_data(as_text=True)

    def obtengo_lista_de_usuarios(self):
        print("Obtengo lista de usuarios desde el body del response")
        self.contenido = json.loads(self.obtengo_contenido())
        return self

    def dado_el_usuario_(self, usuario):
        print("Declaro el usuario", usuario)
        self.database.users.insert_one(usuario)

    def entonces_corroboro_que_el_unico_usuario_es_(self, usuario):
        print("Corroboro que el usuario es", usuario["name"], usuario["lastname"])
        self.assertEqual(usuario['name'], self.contenido[0]['name'])
        self.assertEqual(usuario['lastname'], self.contenido[0]['lastname'])

    def entonces_corroboro_que_el_status_es_OK(self):
        print("Tengo código de respuesta OK (200)")
        self.assertEqual(200, self.response.status_code)

    def limpiar_escenarios(self):
        self.contenido = None
        self.status = None
        self.response = None