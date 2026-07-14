import web
import sqlite3

render = web.template.render('views/productos', base='../layout')


class BorrarProducto:

    def eliminarProducto(self, id_producto: int):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            query = "DELETE FROM productos WHERE id_producto = ?"

            cursor.execute(query, (id_producto,))
            conexion.commit()
            conexion.close()

            return True

        except sqlite3.Error as error:
            print(f"ERROR BorrarProducto 100: {error.args}")
            return False

        except Exception as error:
            print(f"ERROR BorrarProducto 101: {error.args}")
            return False


    def buscarProducto(self, id_producto: int):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            query = "SELECT * FROM productos WHERE id_producto = ?"

            cursor.execute(query, (id_producto,))
            resultado = cursor.fetchone()

            producto = {
                "id_producto": resultado[0],
                "nombre": resultado[1],
                "stock": resultado[2],
                "descripcion": resultado[3],
                "precio": resultado[4]
            }

            conexion.close()
            return producto

        except sqlite3.Error as error:
            print(f"ERROR BorrarProducto 102: {error.args}")
            return {}

        except Exception as error:
            print(f"ERROR BorrarProducto 103: {error.args}")
            return {}


    def GET(self, id_producto: int):
        try:
            mensaje = None
            producto = self.buscarProducto(id_producto)
            return render.borrar_producto(producto, mensaje)
        except Exception as error:
            print(f"ERROR BorrarProducto 104: {error.args}")
            return "UPS, algo fallo"


    def POST(self, id_producto: int):
        try:
            resultado = self.eliminarProducto(id_producto)

            if resultado is False:
                mensaje = "No se pudo eliminar el producto."
                producto = self.buscarProducto(id_producto)
                return render.borrar_producto(producto, mensaje)

            web.ctx.status = '303 See Other'
            web.header('Location', '/lista_productos')
            return ''

        except Exception as error:
            print(f"ERROR BorrarProducto 105: {error.args}")
            return "UPS, algo fallo"