import web

urls = (
    '/', 'controllers.index.Index',
    #Rutas para el modulo proveedores
    '/lista_proveedores', 'controllers.proveedores.lista_proveedores.ListaProveedores',
    '/insertar_proveedor', 'controllers.proveedores.insertar_proveedor.InsertarProveedor',
    '/ver_proveedor/(.*)', 'controllers.proveedores.ver_proveedor.VerProveedor',
    '/borrar_proveedor/(.*)', 'controllers.proveedores.borrar_proveedor.BorrarProveedor',
    '/editar_proveedor/(.*)', 'controllers.proveedores.editar_proveedor.EditarProveedor',

    #Rutas para el modulo clientes
    '/lista_clientes', 'controllers.clientes.lista_clientes.ListaClientes',
    '/insertar_cliente', 'controllers.clientes.insertar_cliente.InsertarCliente',
    '/ver_cliente/(.*)', 'controllers.clientes.ver_cliente.VerCliente', 
    '/borrar_cliente/(.*)', 'controllers.clientes.borrar_cliente.BorrarCliente',
    '/editar_cliente/(.*)', 'controllers.clientes.editar_cliente.EditarCliente',

    #Rutas para el modulo productos
    '/lista_productos', 'controllers.productos.lista_productos.ListaProductos',
    '/insertar_producto', 'controllers.productos.insertar_producto.InsertarProducto',
    '/ver_producto/(.*)', 'controllers.productos.ver_producto.VerProductos', 
    '/borrar_producto/(.*)', 'controllers.productos.borrar_producto.BorrarProducto',
    '/editar_producto/(.*)', 'controllers.productos.editar_producto.EditarProducto'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    web.config.debug = False
    app.run()
