import web

urls = (
    '/', 'controllers.index.Index',
    '/proveedores', 'controllers.proveedores.lista_proveedores.ListaProveedores',
    '/insertar_proveedor', 'controllers.proveedores.insertar_proveedor.InsertarProveedor'
    '/ver_proveedor/(.*)', 'controllers.proveedores.ver_proveedor.VerProveedor' 
    '/borrar_proveedor/(.*)', 'controllers.proveedores.borrar_proveedor.BorrarProveedor'
    '/editar_proveedor/(.*)', 'controllers.proveedores.editar_proveedor.EditarProveedor'

    '/clientes', 'controllers.clientes.lista_clientes.ListaClientes',

    '/productos', 'controllers.productos.lista_productos.ListaProductos',
    '/insertar_producto', 'controllers.producto.insertar_producto.InsertarProducto'
    '/ver_producto/(.*)', 'controllers.producto.ver_producto.VerProductofvg' 
    '/borrar_producto/(.*)', 'controllers.producto.borrar_producto.BorrarProducto'
    '/editar_producto/(.*)', 'controllers.producto.editar_producto.EditarProductp'


)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
