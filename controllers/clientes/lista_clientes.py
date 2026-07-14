import web
import sqlite3

render = web.template.render('views/clientes', base='../layout')

class ListaClientes:

    def consultarClientes(self):
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            query = "SELECT * FROM clientes;"
            cursor.execute(query)
            resultado = cursor.fetchall()

            datos = []
            for fila in resultado:
                cliente = {
                    "id_cliente": fila[0],
                    "nombre": fila[1],
                    "primer_apellido": fila[2],
                    "segundo_apellido": fila[3],
                    "telefono": fila[4],
                }
                datos.append(cliente)

            conexion.close()
            print(datos)
            return datos
        except sqlite3.Error as error:
            print(f"ERROR ListaClientes 100: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR ListaClientes 101: {error.args}")
            return []

    def GET(self):
        try:
            clientes = self.consultarClientes()
            return render.lista_clientes(clientes) # type: ignore
        except Exception as error:
            print(f"ERROR ListaClientes 102: {error.args}")
            return f"Ups, algo falló"