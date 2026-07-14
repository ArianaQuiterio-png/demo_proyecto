import web
import sqlite3

# Configuración del render para las vistas de clientes
render = web.template.render('views/clientes', base='../layout')

class InsertarCliente:

    def guardarCliente(self, cliente: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            nombre = cliente["nombre"]
            primer_apellido = cliente["primer_apellido"]
            segundo_apellido = cliente["segundo_apellido"]
            telefono = cliente["telefono"]

            query = """
            INSERT INTO clientes(
                nombre,
                primer_apellido,
                segundo_apellido,
                telefono
            ) VALUES (?,?,?,?);
            """

            datos = (
                nombre,
                primer_apellido,
                segundo_apellido,
                telefono
            )

            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR InsertarCliente 300: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR InsertarCliente 301: {error.args}")
            return False

    def GET(self):
        try:
            return render.insertar_cliente() # type: ignore
        except Exception as error:
            print(f"ERROR InsertarCliente 302: {error.args}")
            return "UPS, algo fallo"

    def POST(self):
        try:
            formulario = web.input()
            cliente = {
                "nombre": formulario['nombre'],
                "primer_apellido": formulario['primer_apellido'],
                "segundo_apellido": formulario['segundo_apellido'],
                "telefono": formulario['telefono']
            }
            resultado = self.guardarCliente(cliente)

            # Formato de redirección
            web.ctx.status = '303 See Other'
            web.header('Location', '/lista_clientes')
            return ''
        except Exception as error:
            print(f"ERROR InsertarCliente 303: {error.args}")
            return "UPS, algo fallo"