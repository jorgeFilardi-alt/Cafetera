### POST requests de ejemplo, autenticacion:

```bash
curl -X 'POST' \
  'http://localhost:8000/login-test' \
  -H 'Content-Type: application/json' \
  -d '{
  "correo": "admin@gc.com",
  "pwd_hash": "adminpass123"
}'

# Autenticar usuario

curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'Content-Type: application/json' \
  -d '{
  "correo": "admin@gc.com",
  "pwd_hash": "adminpass123"
}'

# Ruta requiere autenticacion (JWT en Headers)

curl -X 'PUT' \
  'http://localhost:8000/proveedor' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb3JyZW8iOiJhZG1pbkBnYy5jb20iLCJpc19hZG1pbiI6MSwiZXhwIjoxNzUwMDc4MzY2LjE2MzU4NX0.CMcsxhr84Kv3WEfvX-XFHocOcrLOpbKpM5ELqvCm8rA' \
  -d '{
  "correo": "admin@gc.com",
  "pwd_hash": "adminpass123"
}'
```

