import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarProveedor:

    def editaProvedor(self, id_proveedor:int):
        try:
            conexion = sqlite3.connect("sql/agenda.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM proveedores WHERE id_proveedor = ?"
            cursor.execute(query,(id_proveedor,))
            resultado = cursor.fetchone()

            proveedor = {
                "id_proveedor":resultado[0],
                "nombre_empresa":resultado[1],
                "correo":resultado[2],
                "telefono":resultado[3],
                "ciudad":resultado[4],
            }
            conexion.close()
            print(proveedor)
            return proveedor
        except sqlite3.Error as error:
            print(f"ERROR 102: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 103: {error.args}")
            return []

    def GET(self,id_proveedor:int):
        print(f"ID_PROVEEDOR: {id_proveedor}")
        proveedor = self.editaProvedor(id_proveedor)
        return render.editar_proveedor(proveedor)