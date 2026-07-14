import web
import sqlite3

render = web.template.render('views/clientes', base='../layout')

class EditarCliente:

    def actualizarCliente(self, cliente: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = """UPDATE clientes
                       SET nombre = ?,
                           primer_apellido = ?,
                           segundo_apellido = ?,
                           telefono = ?
                       WHERE id_cliente = ?;"""
            datos = (cliente["nombre"], cliente["primer_apellido"], 
                     cliente["segundo_apellido"], cliente["telefono"], 
                     cliente["id_cliente"])
            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR EditarCliente 200: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR EditarCliente 201: {error.args}")
            return False

    def buscarCliente(self, id_cliente: int):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM clientes WHERE id_cliente = ?"
            cursor.execute(query, (id_cliente,))
            resultado = cursor.fetchone()
            cliente = {
                "id_cliente": resultado[0],
                "nombre": resultado[1],
                "primer_apellido": resultado[2],
                "segundo_apellido": resultado[3],
                "telefono": resultado[4],
            }
            conexion.close()
            return cliente
        except Exception as error:
            print(f"ERROR EditarCliente 202: {error.args}")
            return {}

    def GET(self, id_cliente: int):
        cliente = self.buscarCliente(id_cliente)
        return render.editar_cliente(cliente)

    def POST(self, id_cliente: int):
        formulario = web.input()
        cliente = {
            "id_cliente": formulario['id_cliente'],
            "nombre": formulario['nombre'],
            "primer_apellido": formulario['primer_apellido'],
            "segundo_apellido": formulario['segundo_apellido'],
            "telefono": formulario['telefono']
        }
        self.actualizarCliente(cliente)
        web.ctx.status = '303 See Other'
        web.header('Location', '/lista_clientes')
        return ''