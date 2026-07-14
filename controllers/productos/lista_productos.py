import web

render = web.template.render('views', base='layout')

db = web.database(
    dbn='sqlite',
    db='sql/ferreteria.db'
)

class ListaProductos:
    def GET(self):
        productos = db.select('productos')
        return render.productos.ver_productos(productos)