-- Datos de prueba para la base de datos: gestion_comercial.
-- Generados por: Gemini 2.5 Pro (version preliminar)

-- Se utiliza la base de datos creada
USE gestion_comercial;

-- 1. Tabla: login
-- Contraseñas de ejemplo. En un sistema real, estas deberían estar hasheadas (ej: con bcrypt).
INSERT IGNORE INTO login (correo, contraseña, es_administrador) VALUES
('admin@gc.com', 'adminpass123', TRUE),
('juan.p@gc.com', 'juanperezpass', FALSE),
('maria.r@gc.com', 'mariarodriguezpass', FALSE),
('carlos.g@gc.com', 'carlosgonzalezpass', FALSE),
('ana.m@gc.com', 'anamartinezpass', FALSE);

-- 2. Tabla: proveedores
INSERT IGNORE INTO proveedores (id_proveedor, nombre, telefono) VALUES
(101, 'Café Tostado S.A.', 29001234),
(102, 'Lácteos del Sur', 26005678),
(103, 'DulceRico Azúcar', 23059012),
(104, 'Insumos Globales', 24083456),
(105, 'Agua Pura SRL', 22007890);

-- 3. Tabla: insumos
INSERT IGNORE INTO insumos (id_insumo, descripcion, tipo, precio_unitario, id_proveedor) VALUES
(1, 'Granos de Café Arábica 1kg', 'Café', 850, 101),
(2, 'Granos de Café Robusta 1kg', 'Café', 720, 101),
(3, 'Leche Entera Larga Vida 1L', 'Lácteo', 55, 102),
(4, 'Leche Descremada Larga Vida 1L', 'Lácteo', 58, 102),
(5, 'Azúcar Blanca Refinada 1kg', 'Endulzante', 60, 103),
(6, 'Edulcorante Líquido 250ml', 'Endulzante', 120, 103),
(7, 'Vasos de Cartón 240ml (x100)', 'Vaso', 250, 104),
(8, 'Removedores de Madera (x500)', 'Accesorio', 180, 104),
(9, 'Agua Mineral sin Gas 6L', 'Agua', 110, 105),
(10, 'Filtros de Papel N°4 (x100)', 'Filtro', 300, 104);

-- 4. Tabla: clientes
INSERT IGNORE INTO clientes (id_cliente, nombre, dirección, telefono, correo) VALUES
(201, 'Oficina Central', 'Av. 18 de Julio 1234', 29011111, 'contacto@oficentral.com'),
(202, 'Coworking Innova', 'Dr. Luis Alberto de Herrera 3365', 26222222, 'info@innova.uy'),
(203, 'Estudio Contable Díaz', 'Rincón 454', 29163333, 'admin@diazcontadores.com'),
(204, 'Clínica Bienestar', 'Bv. Artigas 1122', 27084444, 'recepcion@clinicabienestar.com'),
(205, 'Universidad del Saber', 'Av. Italia 2345', 24875555, 'compras@uds.edu.uy');

-- 5. Tabla: tecnicos
INSERT IGNORE INTO tecnicos (ci, nombre, apellido, telefono) VALUES
(45556667, 'Roberto', 'Morales', 99123456),
(51112223, 'Laura', 'Giménez', 98765432),
(39998887, 'Diego', 'Fernández', 91234876),
(48765432, 'Valentina', 'Sosa', 99888777);

-- 6. Tabla: maquinas
-- Se asume que la dirección de la máquina es la misma que la del cliente, pero podría ser diferente.
INSERT IGNORE INTO maquinas (id_maquina, modelo, id_cliente, dirección_cliente, costo_alquiler_mensual) VALUES
(301, 'Expressa Pro 2000', 201, 'Av. 18 de Julio 1234', 5000),
(302, 'LatteMaster 500', 201, 'Av. 18 de Julio 1234', 6500),
(303, 'FilterCoffee Max', 202, 'Dr. Luis Alberto de Herrera 3365', 4500),
(304, 'Expressa Pro 2000', 203, 'Rincón 454', 5000),
(305, 'Cappuccino Deluxe', 204, 'Bv. Artigas 1122', 7000),
(306, 'Expressa Pro 2000', 205, 'Av. Italia 2345, Cafetería', 5200),
(307, 'LatteMaster 500', 205, 'Av. Italia 2345, Sala Profesores', 6800);

-- 7. Tabla: mantenimientos
INSERT IGNORE INTO mantenimientos (id_mantenimiento, id_maquina, ci_tecnico, tipo, fecha, observarciones) VALUES
(401, 301, 45556667, 'Preventivo', '2025-01-15', 'Limpieza general y descalcificación.'),
(402, 303, 51112223, 'Correctivo', '2025-02-20', 'Se reemplazó la bomba de agua.'),
(403, 302, 45556667, 'Instalación', '2025-03-01', 'Instalación y configuración inicial.'),
(404, 305, 39998887, 'Preventivo', '2025-03-10', 'Revisión de molinillo y grupo de café.'),
(405, 304, 51112223, 'Urgente', '2025-04-05', 'Fuga en manguera de vapor, se sustituyó.'),
(406, 306, 48765432, 'Preventivo', '2025-04-22', 'Limpieza de conductos de leche.'),
(407, 307, 45556667, 'Correctivo', '2025-05-18', 'El panel digital no respondía, se reinició.'),
(408, 301, 39998887, 'Preventivo', '2025-06-12', 'Chequeo de presión y temperatura.');

-- 8. Tabla: registro_consumo
-- Se generan múltiples registros de consumo para distintas maquinas e insumos a lo largo del tiempo.
INSERT IGNORE INTO registro_consumo (id_consumo, id_maquina, id_insumo, fecha, cantidad_usada) VALUES
-- Consumos Máquina 301
(501, 301, 1, '2025-05-02', 2), -- 2 kg de Café Arábica
(502, 301, 3, '2025-05-02', 5), -- 5 L de Leche Entera
(503, 301, 5, '2025-05-03', 1), -- 1 kg de Azúcar
(504, 301, 7, '2025-05-04', 3), -- 300 Vasos
-- Consumos Máquina 302
(505, 302, 2, '2025-05-05', 3), -- 3 kg de Café Robusta
(506, 302, 4, '2025-05-05', 8), -- 8 L de Leche Descremada
-- Consumos Máquina 303
(507, 303, 1, '2025-05-10', 5),
(508, 303, 9, '2025-05-10', 4), -- 4 bidones de Agua
(509, 303, 10, '2025-05-11', 2), -- 200 Filtros
-- Consumos Máquina 304
(510, 304, 1, '2025-05-15', 1),
(511, 304, 6, '2025-05-15', 2), -- 2 Edulcorantes
-- Consumos Máquina 305
(512, 305, 2, '2025-05-20', 4),
(513, 305, 3, '2025-05-20', 10),
(514, 305, 8, '2025-05-21', 1), -- 500 removedores
-- Consumos recientes (Junio 2025)
(515, 301, 1, '2025-06-01', 2),
(516, 301, 3, '2025-06-01', 5),
(517, 302, 2, '2025-06-03', 2),
(518, 307, 1, '2025-06-05', 3),
(519, 307, 4, '2025-06-05', 6),
(520, 303, 1, '2025-06-10', 4);