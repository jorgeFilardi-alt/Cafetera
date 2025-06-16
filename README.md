# Cafetera
Descripcion...
Obligatorio, equipo, etc

## Inicializacion completa
Extractos de todas las secciones
### Front End
```bash
# Terminal 1 (frontend)
npm run dev
```
### Back End
```bash
# Terminal 2 (mysql)
docker-compose -f /Server/sql/docker-compose.yml up -d
```
```bash
# Terminal 3 (api, endpoint)
cd Server
source venv/bin/activate
python sql/populate.py 1
uvicorn main:app --reload
```
[Backend (python + fastapi)](#inicializacion-backend)

## Requirements:

# Client (React + Vite)

## Inicializacion Frontend

- npm i to install dependencies
- npm run dev
- Go to ´http://localhost:3000´

# Server (Python + FastAPI)
Mencion a decisiones, etc, consideraciones ...
Toda ejecucion en Server, considerada dentro de la carpeta Server `cd Server`

## Inicializacion Backend
```bash
cd Server
source venv/bin/activate
# fastapi => uvicorn
uvicorn main:app --reload
# Instancia docker de mysql
docker-compose up -d # off: ...ose down
```
Go to ´http://127.0.0.1:8000/docs#/´ to see swagger and specification of the endpoinds.

## Dependencias:
Utilizamos fastapi, uvicorn para ejecutar una instancia, docker-compose para mysql local.

Python y venv (enviroment context)
### Instalacion

```bash
# Crear python venv (This will create a virtual enviroment for the project)
python -m venv venv

# Activate the venv (exit: `deactivate`)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## MySQL

Compartir servidor, podriamos usar docker (la entrega no especifica). Por simplicidad, correra todo localmente (requiriendo una instancia de mysql con las mismas caracteristicas). 

### Requisitos:

- Instancia MySQL en `127.0.0.1` ([docker-compose](#instalacion-docker-compose))
- Base de datos `gestion_comercial`
- Usuario de mysql `root`, pwd `root`
- Dependencias del repo (pip, ...)

### Instalacion Ubuntu

```bash
sudo apt update
sudo apt install mysql-server

# Iniciar
sudo systemctl start mysql
sudo systemctl enable mysql
```
### Instalacion Docker Compose
```bash
# Instalar Docker (final: reiniciar terminal)
sudo apt install docker.io -y # Instalar Docker
sudo apt install docker-compose -y # Instalar Docker Compose
sudo usermod -aG docker ${USER} # Anadir al grupo de docker

# Init
docker-compose up -d
```

### Creaer Variables de entorno
Para protejer los datos de nuestros usuarios debemos protejer nuestras claves privadas, de esta manera verificar la firma del payload mandado por el usuario
```bash
echo -e 'JWT_SECRET="si_no_si_si"\nJWT_ALGORITHM="HS256"\nJWT_EXPIRATION=60 * 60 * 12' > .env
```

### Generar Datos de prueba

Generar script (ejecutando linea por linea de los archivos .sql)
```bash
cd Server
source venv/bin/activate
python sql/populate.py 2 # arg `2` = Reset
```

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

## DAL layer (auth y sanitize statements)

# Bibliografia

TODO: citar comandos?
pydantic, basemodel??