import web
import sqlite3

render = web.template.render('views/productos', base='../layout')

class InsertarProducto:

    def guardarProducto(self, producto: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            nombre = producto["nombre"]
            stock = producto["stock"]
            descripcion = producto["descripcion"]
            precio = producto["precio"]

            query = """
                INSERT INTO productos(
                    nombre,
                    stock,
                    descripcion,
                    precio
                ) VALUES (?,?,?,?);
            """

            datos = (
                nombre,
                stock,
                descripcion,
                precio
            )

            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()
            return True

        except sqlite3.Error as error:
            print(f"ERROR InsertarProducto 300: {error.args}")
            return False

        except Exception as error:
            print(f"ERROR InsertarProducto 301: {error.args}")
            return False

    def GET(self):
        try:
            return render.nuevo_producto()
        except Exception as error:
            print(f"ERROR InsertarProducto 302: {error.args}")
            return "UPS, algo fallo"

    def POST(self):
        try:
            formulario = web.input()

            producto = {
                "nombre": formulario["nombre"],
                "stock": formulario["stock"],
                "descripcion": formulario["descripcion"],
                "precio": formulario["precio"]
            }

            self.guardarProducto(producto)

            web.ctx.status = '303 See Other'
            web.header('Location', '/lista_productos')
            return ''

        except Exception as error:
            print(f"ERROR InsertarProducto 303: {error.args}")
            return "UPS, algo fallo"