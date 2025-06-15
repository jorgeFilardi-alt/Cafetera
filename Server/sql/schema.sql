-- Schema / Setup / Tablas
CREATE DATABASE gestion_comercial;
USE gestion_comercial;

CREATE TABLE login(
    correo VARCHAR(20) PRIMARY KEY,
    contraseña VARCHAR(100),
    es_administrador BOOLEAN,
    CHECK (LENGTH(contraseña) > 8)
);
CREATE TABLE proveedores(
    id_proveedor INT PRIMARY KEY,
    nombre VARCHAR(20),
    telefono INT --Se reemplaza la columna sugerida "contacto" por "telefono" para evitar distintos tipos de dato de contacto
);
CREATE TABLE insumos(
    id_insumo INT PRIMARY KEY,
    descripcion VARCHAR(50),
    tipo VARCHAR(20),
    precio_unitario INT,
    id_proveedor INT,
    Foreign Key (id_proveedor) REFERENCES proveedores(id_proveedor)
);
CREATE TABLE clientes(
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(20),
    dirección VARCHAR(50),
    telefono INT,
    correo VARCHAR(50)
);
CREATE TABLE maquinas(
    id_maquina INT PRIMARY KEY,
    modelo varchar(20),
    id_cliente INT NOT NULL,
    dirección_cliente varchar(50),
    costo_alquiler_mensual INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
CREATE TABLE registro_consumo(
    id_consumo INT PRIMARY KEY,
    id_maquina INT NOT NULL,
    id_insumo INT NOT NULL,
    fecha DATE,
    cantidad_usada INT,
    Foreign Key (id_maquina) REFERENCES maquinas(id_maquina),
    Foreign Key (id_insumo) REFERENCES insumos(id_insumo)
);
CREATE TABLE tecnicos(
    ci INT PRIMARY KEY,
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    telefono INT
);
CREATE TABLE mantenimientos(
    id_mantenimiento INT PRIMARY KEY,
    id_maquina INT NOT NULL,
    ci_tecnico INT NOT NULL,
    tipo VARCHAR(20),
    fecha DATE,
    observarciones VARCHAR(50),
    Foreign Key (id_maquina) REFERENCES maquinas(id_maquina),
    Foreign Key (ci_tecnico) REFERENCES tecnicos(ci)
);