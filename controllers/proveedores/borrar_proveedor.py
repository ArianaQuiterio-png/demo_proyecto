import web
import sqlite3

render = web.template.render('views/proveedores', base='../layout')

class BorrarProveedor:

    def eliminarProveedor(self, id_proveedor: int):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            query = "DELETE FROM proveedores WHERE id_proveedor = ?"
            cursor.execute(query, (id_proveedor,))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR BorrarProveedor 100: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR BorrarProveedor 101: {error.args}")
            return False

    def buscarProveedor(self, id_proveedor: int):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            
            query = "SELECT * FROM proveedores WHERE id_proveedor = ?"
            cursor.execute(query, (id_proveedor,))
            resultado = cursor.fetchone()

            proveedor = {
                "id_proveedor": resultado[0],
                "nombre_empresa": resultado[1],
                "correo": resultado[2],
                "telefono": resultado[3],
                "ciudad": resultado[4]
            }
            conexion.close()
            print(proveedor)
            return proveedor
        except sqlite3.Error as error:
            print(f"ERROR BorrarProveedor 102: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR BorrarProveedor 103: {error.args}")
            return {}

    def GET(self, id_proveedor: int):
        try:
            mensaje = None
            proveedor = self.buscarProveedor(id_proveedor)
            return render.borrar_proveedor(proveedor, mensaje) # type: ignore
        except Exception as error:
            print(f"ERROR BorrarProveedor 104: {error.args}")
            return f"Algo fallo, estamos trabajando en solucionarlo"

    def POST(self, id_proveedor: int):
        try:
            resultado = self.eliminarProveedor(id_proveedor)
            if resultado is False:

                mensaje = "El registro no se puede eliminar porque está asignado en otra tabla."
                proveedor = self.buscarProveedor(id_proveedor)
                return render.borrar_proveedor(proveedor, mensaje)  # type: ignore
            else:
                web.ctx.status = '303 See Other'
                web.header('Location', '/lista_proveedores')
                return ''
        except Exception as error:
            print(f"ERROR BorrarProveedor 105: {error.args}")
            return f"UPS, algo fallo"