# Comunicacion cliente <=> API

## **Endpoints Publicos**
### Tabla tecnicos
```bash
# Request:
curl -X 'GET' \
  'http://localhost:8000/tecnicos' \
  -H 'Content-Type: application/json' \
```
```json
// JSON Response:
[
  [39998887,"Diego","Fernández",91234876],
  [45556667,"Roberto","Morales",99123456],
  [48765432,"Valentina","Sosa",99888777],
  [51112223,"Laura","Giménez",98765432]
]
```
### Tecnico Roberto Morales
```bash
# Request:
curl -X 'GET' 'http://localhost:8000/tecnico/45556667' \
  -H 'Content-Type: application/json' \
```
```json
// JSON Response:
[
  [45556667, "Roberto", "Morales", 99123456]
]
```

## **Autenticacion**
### Registro
Registrar usuario
```bash
# Request:
curl -X 'POST'   'http://localhost:8000/register'   -H 'Content-Type: application/json'   -d '{
  "correo": "admin@marloy.com",
  "pwd_hash": "marloy1234"
}'
```



### Login
Generar token de autenticacion para usuario
```bash
# Request:
curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'Content-Type: application/json' \
  -d '{
  "correo": "admin@marloy.com",
  "pwd_hash": "marloy1234"
}'
```
```json
// JSON Response:
{
  "jwt": "Bearer <token>",
  "is_auth": true,
  "es_administrador": 1,
  "correo": "admin@marloy.com"
}
```
### Uso de Token
HTTPOnly cookie o Authorization Header
```bash
# Request:
  -H 'Authorization: Bearer <token>'
```

## **Endpoints Privados**
POST requests de ejemplo, con autenticacion:

### Query clientes
```bash
# Request:
curl -X 'GET' 'http://localhost:8000/cliente/201' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <token>'
```
```json
// JSON Response:
[
  [201, "Oficina Central", "Av. 18 de Julio 1234", 29011111, "contacto@oficentral.com"]
]
```

### Update (solo administradores)
Ruta autenticada requiere Bearer (JWT en Headers) y usuario administrador, actualizacion de proveedor:

```bash
# Request:
curl -X 'PUT' \
  'http://localhost:8000/proveedor' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <token>' \
  -d '{
  "id_proveedor": "102",
  "telefono": "1234567"
}'
```
```json
// JSON Response:
[
  [102,"Lácteos del Sur",1234567,1]
]
```