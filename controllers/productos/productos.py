import web
import sqlite3

render = web.template.render("views/")

class Productos:
    def GET(self):
        conexion = sqlite3.connect("sql/ferreteria.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()

        return render.productos.productos(productos)

class NuevoProducto:

    def GET(self):
        return render.productos.nuevo()

    def POST(self):

        datos = web.input()
        conexion = sqlite3.connect("sql/ferreteria.db")
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO productos(nombre,stock,descripcion,precio) VALUES(?,?,?,?)",
            (datos.nombre, datos.stock, datos.descripcion, datos.precio)
        )
        conexion.commit()
        conexion.close()
        raise web.seeother("/productos")

class BorrarProducto:

    def GET(self):
        datos = web.input(id=None)
        conexion = sqlite3.connect("sql/ferreteria.db")
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM productos WHERE id_producto=?",
            (datos.id,)
        )
        conexion.commit()
        conexion.close()
        
        raise web.seeother("/productos")