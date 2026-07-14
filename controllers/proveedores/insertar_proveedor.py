import web
import sqlite3

# Configuración del render para las vistas de proveedores
render = web.template.render('views/proveedores', base='../layout')

class InsertarProveedor:

    def guardarProveedor(self, proveedor: dict) -> bool:
        try:
            conexion = sqlite3.connect("sql/ferreteria.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            nombre_empresa = proveedor["nombre_empresa"]
            correo = proveedor["correo"]
            telefono = proveedor["telefono"]
            ciudad = proveedor["ciudad"]

            # CORREGIDO: Se quitó la coma después de 'ciudad'
            query = """
                INSERT INTO proveedores(
                    nombre_empresa,
                    correo,
                    telefono,
                    ciudad
                ) VALUES (?,?,?,?);
                """
                
            # CORREGIDO: Se quitó la coma final después de 'ciudad'
            datos = (
                nombre_empresa,
                correo,
                telefono,
                ciudad
            )
            
            cursor.execute(query, datos)
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.Error as error:
            print(f"ERROR InsertarProveedor 300: {error.args}")
            return False
        except Exception as error:
            print(f"ERROR InsertarProveedor 301: {error.args}")
            return False

    def GET(self):
        try:
            return render.insertar_proveedor() # type: ignore
        except Exception as error:
            print(f"ERROR InsertarProveedor 302: {error.args}")
            return f"UPS, algo fallo"

    def POST(self):
        try:
            formulario = web.input()
            proveedor = {
                "nombre_empresa" : formulario['nombre_empresa'],
                "correo" : formulario['correo'],
                "telefono" : formulario['telefono'],
                "ciudad" : formulario['ciudad'],
            }
            resultado = self.guardarProveedor(proveedor)
            
            # Formato de redirección manual del profesor
            web.ctx.status = '303 See Other'
            web.header('Location', '/lista_proveedores')
            return ''
        except Exception as error:
            print(f"ERROR InsertarProveedor 303: {error.args}")
            return f"UPS, algo fallo"