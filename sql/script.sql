CREATE TABLE clientes(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apellido TEXT NOT NULL,
    telefono TEXT NOT NULL
);

CREATE TABLE proveedores(
    id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_empresa TEXT NOT NULL,
    correo TEXT NOT NULL,
    telefono TEXT NOT NULL,
    ciudad TEXT NOT NULL
);

CREATE TABLE productos(
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    stock INTEGER NOT NULL,
    descripcion TEXT NOT NULL,
    precio FLOAT NOT NULL
);

INSERT INTO clientes(nombre, primer_apellido, segundo_apellido, telefono)
VALUES 
('Angel','Escorcia','Quiterio','111111111');

INSERT INTO proveedores(nombre_empresa, correo, telefono, ciudad)
VALUES
('Truper', 'truper@mail', '222222222', 'Mexico');

INSERT INTO productos(nombre, stock, descripcion, precio)
VALUES
('Martillo', 32, 'Cabeza de acero y mango de madera', 150);