# Cafeteras Marloy

> La empresa “Cafés Marloy” planea implementar un sistema administrativo para gestionar
sus máquinas expendedoras de café distribuidas en distintos clientes, así como el control de
insumos, proveedores, técnicos y consumos. 
[<small>Consigna.pdf</small>](./Consigna.pdf)

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

### API web
Utilizamos fastapi (alternativa flask, requiere mas configuracion), ejecutamos una instancia con uvicorn, (alternativa: hypercorn, moderno standard ASGI).

### Base de datos

Utilizamos docker-compose con su archivo de configuracion correspondiente para generar un contenedor mysql, nos parece una solucion mas estandard y comoda que una instancia mysql en local.

Definimos condiciones por defecto del contenedor, MySQL en `127.0.0.1` ([docker-compose](#verificar-comandos-utiles)), usuario de mysql `root`, pwd `root` (acceso total), puerto mapeado a mquina local `-p 3307` (no 3306).

### Autenticacion JWT y vEnv
Para protejer los datos de nuestros usuarios debemos protejer nuestras claves privadas, de esta manera verificar la firma del payload mandado por el usuario.

Agregamos venv (enviroment context) asegurar configuracion interna privada no sea expuesta.

### Estructura de datos

Type-safe client (schema models) Tipamos nuestro esquema de datos con `pydantic`, consideramos tiene mejores metodos que una de sus alternativas: `@dataclass` (modificar estructuras, convertir a parametros opcionales o todos requeridos).

## Estructura Respuesta HTTP
Peticiones / metodos web dentro del protocolo http: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`. Sus estructura esperadas, de la response y request.

GET (Queries) / PUT (Updates) / POST (CREATES)
Si exitoso, responde con el recurso actualizado. Para queries singulares / unitarias el JSON de respuesta contiene una misma estructura que para queries con multiples entries / records (tablas / reportes).

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