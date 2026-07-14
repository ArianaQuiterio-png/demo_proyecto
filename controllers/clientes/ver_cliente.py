import web
import sqlite3

render = web.template.render('views/clientes', base='../layout')

class VerCliente:

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
            print(cliente)
            return cliente
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return []

    def GET(self, id_cliente: int):
        print(f"ID_CLIENTE: {id_cliente}")
        cliente = self.buscarCliente(id_cliente)
        return render.ver_cliente(cliente) # type: ignore