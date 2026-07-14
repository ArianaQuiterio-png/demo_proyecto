import web
import sqlite3

render = web.template.render('views/clientes', base='../layout')

class BorrarCliente:

    def eliminarCliente(self, id_cliente: int):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            query = "DELETE FROM clientes WHERE id_cliente = ?"
            cursor.execute(query, (id_cliente,))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR BorrarCliente 100: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR BorrarCliente 101: {error.args}")
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
            print(f"ERROR BorrarCliente 102: {error.args}")
            return {}

    def GET(self, id_cliente: int):
        try:
            mensaje = None
            cliente = self.buscarCliente(id_cliente)
            return render.borrar_cliente(cliente, mensaje) # type: ignore
        except Exception as error:
            print(f"ERROR BorrarCliente 104: {error.args}")
            return "Algo fallo, estamos trabajando en solucionarlo"

    def POST(self, id_cliente: int):
        try:
            resultado = self.eliminarCliente(id_cliente)
            if resultado is False:
                mensaje = "El registro no se puede eliminar porque esta asignado en otra tabla."
                cliente = self.buscarCliente(id_cliente)
                return render.borrar_cliente(cliente, mensaje) # type: ignore
            else:
                web.ctx.status = '303 See Other'
                web.header('Location', '/lista_clientes')
                return ''
        except Exception as error:
            print(f"ERROR BorrarCliente 105: {error.args}")
            return "UPS, algo fallo"