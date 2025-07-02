# Cafeteras Marloy

> La empresa “Cafés Marloy” planea implementar un sistema administrativo para gestionar
sus máquinas expendedoras de café distribuidas en distintos clientes, así como el control de
insumos, proveedores, técnicos y consumos. [<small></small>](./Consigna.pdf)

## Inicializacion Rapida
Extractos de todas las secciones, requisito previos: [Instalacion Backend](#instalacion), Instalacion Front End

```bash
# Terminal 1 (frontend)
cd Client
npm run dev
```

Asumiendo contenedor `mysql-server` ejecutandose de fondo [docker-compose](#ubuntu)
```bash
# Terminal 2 (backend: api)
cd Server
source venv/bin/activate
uvicorn main:app --reload
```
[Backend (python + fastapi)](#inicializacion-backend)

# Frontend <small>(React + Vite)</small>
Decidimos react + vite

## Inicializacion Frontend

- npm i to install dependencies
- npm run dev
- Go to ´http://localhost:3000´

# Backend <small>(Python + FastAPI)</small>
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
# Instalar docker (reiniciar terminal)
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo usermod -aG docker ${USER}
```

```bash
# 1 Contenedor mySQL

cd sql
docker-compose up -d

# 2 Entorno python

python3.13 -m venv venv
source venv/bin/activate
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
source venv/bin/activate
pip install -r requirements.txt

# 3 Popular db con datos de prueba

cd sql
python populate.py 2 
```
> Sequoia - 15.2

### Windows
Requisitos previos:
- Instalar [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)
- python (v3.13)

```bash
# 1 Contenedor mySQL

cd sql
docker-compose up -d

# Crear entorno python
python -m venv venv
venv/Scripts/Activate.ps1
pip install -r requirements.txt

# 3 Popular db con datos de prueba

cd sql
python populate.py 2 
```
> Windows 11 (2025)

## Verificar (comandos utiles)

### MySQL docker-compose
```bash
# Entrar a dcoker-compose
docker exec -it mysql-server bash

# mysql Shell (pwd: `root`)
mysql -u root -p
```
Ejecutamos comandos SQL, `USE gestion_comercial;` (previamente)

### Comunicacion con la API:

1. Queries a rutas publicas [<small>Comandos CURL</small>](/Server/README.md#endpoints-publicos)
2. Autenticar usuario, get token [<small>Comandos CURL</small>](/Server/README.md#autenticacion)
3. Updates y rutas privadas [<small>Comandos CURL</small>](/Server/README.md#endpoints-privados)

# Anexo

- [Memoria]()
- [Bitacora]()

TODO: citar comandos? fastapi docs
pydantic, basemodel?? / REEMPLZADO con dataclass
HTTPException, fastapi (parametros etc)