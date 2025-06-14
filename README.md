# Cafetera

## Requirements:


## Client (React + Vite)

### How to run:

- npm i to install dependencies
- npm run dev
- Go to ´http://localhost:3000´

## Server (Python + FastAPI)

### How to run:

- Create a venv with ´python -m venv venv´ (This will create a virtual enviroment for the project)
- Activate the venv with ´.\venv\Scripts\activate.bat´
- Install dependencies ´pip install -r requirement.txt´
- Run api with ´uvicorn main:app --reload´
- Go to ´http://127.0.0.1:8000/docs#/´ to see swagger and specification of the endpoinds.

### MySQL

Compartir servidor, podriamos usar docker (la entrega no especifica). Por simplicidad, correra todo localmente (requiriendo una instancia de mysql con las mismas caracteristicas). Requisitos:

- MySQL Instalado
- Base de datos `gestion_comercial`
- Usuario de mysql `root`, pwd `root`
- Dependencias del repo (pip, ...)

## Gerneral Architecture Diagram:
