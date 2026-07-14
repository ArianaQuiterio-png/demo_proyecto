import web
import sqlite3

render = web.template.render("views/proveedores", base="../layout")


class EditarProveedor:

    def actualizarProveedor(self, proveedor: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            id_proveedor = proveedor["id_proveedor"]
            nombre_empresa = proveedor["nombre_empresa"]
            correo = proveedor["correo"]
            telefono = proveedor["telefono"]
            ciudad = proveedor["ciudad"]

            query = """UPDATE proveedores
                SET nombre_empresa = ?,
                correo = ?,
                telefono = ?,
                ciudad = ?
                WHERE id_proveedor = ?;
                """
            datos = (
                nombre_empresa,
                correo,
                telefono,
                ciudad,
                id_proveedor
            )
            cursor.execute(query, datos)
            conexion.commit()
            return True
        except sqlite3.Error as error:
            print(f"ERROR EditarProveedor 200: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR EditarProveedor 201: {error.args}")
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
                "ciudad": resultado[4],
            }
            conexion.close()
            print(proveedor)
            return proveedor
        except sqlite3.Error as error:
            print(f"ERROR EditarProveedor 202: {error.args}")
            return {}
        except Exception as error:
            print(f"ERROR EditarProveedor 203: {error.args}")
            return {}

    def GET(self, id_proveedor: int):
        try:
            print(f"ID_PROVEEDOR: {id_proveedor}")
            proveedor = self.buscarProveedor(id_proveedor)
            return render.editar_proveedor(proveedor) # type: ignore
        except Exception as error:
            print(f"ERROR EditarProveedor 204: {error.args}")
            return f"UPS, algo fallo"

    def POST(self, id_proveedor: int):
        try:
            formulario = web.input()
            proveedor = {
                "id_proveedor": formulario["id_proveedor"],
                "nombre_empresa": formulario["nombre_empresa"],
                "correo": formulario["correo"],
                "telefono": formulario["telefono"],
                "ciudad": formulario["ciudad"],
            }
            resultado = self.actualizarProveedor(proveedor)
            web.ctx.status = "303 See Other"
            web.header("Location", "/lista_proveedores")
            return ""
        except Exception as error:
            print(f"ERROR EditarProveedor 205: {error.args}")
            return f"UPS, algo fallo"