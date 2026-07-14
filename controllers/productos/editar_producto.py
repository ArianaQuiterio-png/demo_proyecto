import web
import sqlite3

render = web.template.render("views/productos", base="../layout")


class EditarProducto:

    def actualizarProducto(self, producto: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            id_producto = producto["id_producto"]
            nombre = producto["nombre"]
            stock = producto["stock"]
            descripcion = producto["descripcion"]
            precio = producto["precio"]

            query = """
                UPDATE productos
                SET nombre = ?,
                    stock = ?,
                    descripcion = ?,
                    precio = ?
                WHERE id_producto = ?;
            """

            datos = (
                nombre,
                stock,
                descripcion,
                precio,
                id_producto
            )

            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()
            return True

        except sqlite3.Error as error:
            print(f"ERROR EditarProducto 200: {error.args}")
            return False

        except Exception as error:
            print(f"ERROR EditarProducto 201: {error.args}")
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
                "precio": resultado[4],
            }

            conexion.close()
            return producto

        except sqlite3.Error as error:
            print(f"ERROR EditarProducto 202: {error.args}")
            return {}

        except Exception as error:
            print(f"ERROR EditarProducto 203: {error.args}")
            return {}


    def GET(self, id_producto: int):
        producto = self.buscarProducto(id_producto)
        return render.editar_producto(producto)


    def POST(self, id_producto: int):
        formulario = web.input()

        producto = {
            "id_producto": formulario["id_producto"],
            "nombre": formulario["nombre"],
            "stock": formulario["stock"],
            "descripcion": formulario["descripcion"],
            "precio": formulario["precio"],
        }

        self.actualizarProducto(producto)

        web.ctx.status = "303 See Other"
        web.header("Location", "/lista_productos")
        return ""