CREATE DATABASE Obligatorio;
USE Obligatorio;
CREATE TABLE login(
    correo VARCHAR(20) PRIMARY KEY,
    contraseña VARCHAR(100),
    es_administrador BOOLEAN,
    CHECK (LENGTH(contraseña) > 8)
);
CREATE TABLE proveedores(
    id_proveedor INT PRIMARY KEY,
    nombre VARCHAR(20),
    teléfono INT --Se reemplaza la columna sugerida "contacto" por "teléfono" para evitar distintos tipos de dato de contacto
);
CREATE TABLE insumos(
    id_insumo INT PRIMARY KEY,
    descripción VARCHAR(50),
    tipo VARCHAR(20),
    precio_unitario INT,
    id_proveedor INT,
    Foreign Key (id_proveedor) REFERENCES proveedores(id_proveedor)
);
CREATE TABLE clientes(
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(20),
    dirección VARCHAR(50),
    teléfono INT,
    correo VARCHAR(50)
);
CREATE TABLE máquinas(
    id_máquina INT PRIMARY KEY,
    modelo varchar(20),
    id_cliente INT NOT NULL,
    dirección_cliente varchar(50),
    costo_alquiler_mensual INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
CREATE TABLE registro_consumo(
    id_consumo INT PRIMARY KEY,
    id_máquina INT NOT NULL,
    id_insumo INT NOT NULL,
    fecha DATE,
    cantidad_usada INT,
    Foreign Key (id_máquina) REFERENCES máquinas(id_máquina),
    Foreign Key (id_insumo) REFERENCES insumos(id_insumo)
);
CREATE TABLE técnicos(
    ci INT PRIMARY KEY,
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    teléfono INT
);
CREATE TABLE mantenimientos(
    id_mantenimiento INT PRIMARY KEY,
    id_máquina INT NOT NULL,
    ci_técnico INT NOT NULL,
    tipo VARCHAR(20),
    fecha DATE,
    observarciones VARCHAR(50),
    Foreign Key (id_máquina) REFERENCES máquinas(id_máquina),
    Foreign Key (ci_técnico) REFERENCES técnicos(ci)
);