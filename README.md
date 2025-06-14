# Cafetera
Descripcion...
Obligatorio, equipo, etc

## Inicializacion completa
Extractos de todas las secciones
### Front End
```bash
# 
```
### Back End
```bash
cd Server
docker-compose up -d
source venv/bin/activate 
uvicorn main:app --reload
```
[Extracto de](#inicializacion-backend)

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
docker-compose up -d
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

- Instancia MySQL en `127.0.0.1`
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
### Generar Datos de prueba
```bash
# Eje
```

# Bibliografia

TODO: citar comandos?
