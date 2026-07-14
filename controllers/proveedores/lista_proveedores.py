import web
import sqlite3

render = web.template.render('views/proveedores', base='../layout')

class ListaProveedores:

    def consultarProveedores(self):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM proveedores;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                proveedor = {
                    "id_proveedor":fila[0],
                    "nombre_empresa":fila[1],
                    "correo":fila[2],
                    "telefono":fila[3],
                    "ciudad":fila[4],
                }
                datos.append(proveedor)

            conexion.close()
            print(datos)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return []

    def GET(self):
        proveedores = self.consultarProveedores()
        return render.lista_proveedores(proveedores)