# Cafeteras Marloy
Descripcion...
Obligatorio, equipo, etc

## Inicializacion Rapida
Extractos de todas las secciones, requisito previos: [Instalacion Backend](#instalacion), Instalacion Front End
### Front End
```bash
# Terminal 1 (frontend)
npm run dev
```
### Back End
```bash
# Terminal 2 (mysql)
cd Server/sql
docker-compose up -d 
```
[docker-compose setup](#instalacion-docker-compose)
```bash
# Terminal 3 (api, endpoint)
cd Server
source venv/bin/activate
python sql/populate.py 2
uvicorn main:app --reload
```
[Backend (python + fastapi)](#inicializacion-backend)

# Client (React + Vite)
Decidimos react + vite

## Inicializacion Frontend

- npm i to install dependencies
- npm run dev
- Go to ´http://localhost:3000´

# Server (Python + FastAPI)
Mencion a decisiones, etc, consideraciones ...

## **Dependencias:**
Utilizamos fastapi, uvicorn para ejecutar una instancia, docker-compose para mysql local.

#### Estructura http () + fastapi uvicorn
Peticiones / metodos web dentro del protocolo http: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`. Sus estructura esperadas, de la response y request.

PUT (Updates) / POST (CREATES)
Si exitoso, responde con el recurso actualizado.
En fallo, responde con error.

### Python mySQL
Requisitos parte de propuesta obligatorio. Condiciones, instancia MySQL en `127.0.0.1` ([docker-compose](#instalacion-docker-compose)), usuario de mysql `root`, pwd `root` (acceso total), puerto mapeado a mquina local `-p 3307` (no 3306).

Type-safe client (schema models) Tipamos nuestro esquema de datos a `@dataclass`.

### Docker Compose
Compartir servidor, podriamos usar docker (la entrega no especifica). Por simplicidad, correra todo localmente (requiriendo una instancia de mysql con las mismas caracteristicas). 

### JWT vEnv
Para protejer los datos de nuestros usuarios debemos protejer nuestras claves privadas, de esta manera verificar la firma del payload mandado por el usuario.

Agregamos venv (enviroment context) asegurar configuracion interna privada.

## **Instalacion:**
Dentro del contexto de ejecucion `./Server` (definimos pasos de instalacion). Utilizamos version de **python 3.13+** (syntaxis en codebase). Generamos la base de datos con  `populate.py` (ejecutando linea por linea de los archivos .sql)

### Ubuntu
```bash
# Instalar docker
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo usermod -aG docker ${USER} # privilegios USER
# Reinciar terminal

# 1 Contenedor mySQL

cd sql
docker-compose up -d

# 2 Entorno python

python3.13 -m venv venv
# Activar entorno
source venv/bin/activate
# Instalar dependencias
pip install -r requirements.txt

# 3 Popular db con datos de prueba

python3.13 sql/populate.py 2 # arg `2` = Reset

```
> Debian - 25.04 (Plucky Puffin)

### MacOs
Requisitos previos:
- Instalar [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/)
- python (v3.13) (dentro de venv usar `python` no `python3`)

```bash
# 1 Contenedor mySQL

cd sql
docker-compose up -d

# 2 Entorno python

python3 -m venv venv
# Activar entorno
source venv/bin/activate
# Instalar dependencias
pip install -r requirements.txt

# 3 Popular db con datos de prueba

cd sql
python populate.py 2 
```
> Sequoia - 15.2

### Windows


## **2. Testing:**

Entrar a mysql en docker-compose
```bash
# Entrar a dcoker-compose
docker exec -it mysql-server bash

# mysql Shell (pwd: `root`)
mysql -u root -p
```

POST request con autenticacion:
```bash
curl -X 'POST' \
  'http://localhost:8000/login-test' \
  -H 'Content-Type: application/json' \
  -d '{
  "correo": "admin@gc.com",
  "pwd_hash": "adminpass123"
}'
```

### POST requests de ejemplo, autenticacion:

```bash
# Ruta normal

curl -X 'GET' \
  'http://localhost:8000/cliente?id_cliente=201' \
  -H 'Content-Type: application/json' \

```
```bash
# Registrar usuario

curl -X 'POST'   'http://localhost:8000/register'   -H 'Content-Type: application/json'   -d '{
  "correo": "admin10@gc.com",
  "pwd_hash": "adminpass123"
}'

# Generar token de autenticacion para usuario

curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'Content-Type: application/json' \
  -d '{
  "correo": "admin@gc.com",
  "pwd_hash": "adminpass123"
}'

```

Ruta autenticada requiere Bearer (JWT en Headers)
```bash

curl -X 'PUT' \
  'http://localhost:8000/proveedor' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3JyZW8iOiJhZG1pbkBnYy5jb20iLCJlc19hZG1pbmlzdHJhZG9yIjoxLCJleHBpcmVzIjoxNzUxMDA0OTMyLjU3NDc3OX0.uwXAsU03_XhfXjVfCfo6MGe7TICAHNEaI2WRZm33QA8' \
  -d '{
  "id_proveedor": "102",
  "telefono": "1234567"
}'
```

# Bibliografia

TODO: citar comandos? fastapi docs
pydantic, basemodel?? / REEMPLZADO con dataclass
HTTPException, fastapi (parametros etc)