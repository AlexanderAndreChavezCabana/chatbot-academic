# 📦 Deployment Guide - Chatbot UNASAM

## Opciones de Despliegue

### 1. **Local (Desarrollo)**

#### Instalación rápida:
```bash
# Clonar o descargar el proyecto
cd chatbot-academic

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Entrenar modelo
rasa train

# Terminal 1: Servidor de acciones
rasa run actions

# Terminal 2: Chatbot interactivo
rasa shell
```

### 2. **API REST (Servidor)**

```bash
# Terminal 1: Servidor de acciones
rasa run actions

# Terminal 2: API REST
rasa run --enable-api --port 5005

# Terminal 3: Hacer request
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola"}'
```

### 3. **Docker**

#### Crear Dockerfile:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN rasa train

EXPOSE 5005 5055

CMD ["rasa", "run", "--enable-api", "--port", "5005"]
```

#### Construir y ejecutar:
```bash
# Construir imagen
docker build -t unasam-chatbot .

# Ejecutar contenedor
docker run -p 5005:5005 -p 5055:5055 unasam-chatbot
```

### 4. **Linux Server (Ubuntu/Debian)**

#### Instalación en servidor:
```bash
# 1. Conectarse al servidor
ssh usuario@servidor.com

# 2. Instalar dependencias del sistema
sudo apt-get update
sudo apt-get install python3.10 python3-pip python3-venv

# 3. Clonar repositorio
git clone <tu-repo>
cd chatbot-academic

# 4. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 5. Instalar RASA
pip install -r requirements.txt

# 6. Entrenar modelo
rasa train

# 7. Crear servicio systemd
sudo nano /etc/systemd/system/unasam-chatbot.service
```

#### Archivo systemd:
```ini
[Unit]
Description=UNASAM Chatbot
After=network.target

[Service]
Type=simple
User=chatbot
WorkingDirectory=/home/chatbot/chatbot-academic
ExecStart=/home/chatbot/chatbot-academic/venv/bin/rasa run --enable-api --port 5005
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### Activar servicio:
```bash
sudo systemctl daemon-reload
sudo systemctl enable unasam-chatbot
sudo systemctl start unasam-chatbot
sudo systemctl status unasam-chatbot
```

### 5. **Heroku**

#### 1. Crear Procfile:
```
web: rasa run --enable-api --port $PORT
```

#### 2. Crear runtime.txt:
```
python-3.10.0
```

#### 3. Deploy:
```bash
heroku create unasam-chatbot
git push heroku main
```

### 6. **AWS EC2**

#### Pasos:
1. Crear instancia EC2 (Ubuntu 20.04)
2. Conectarse: `ssh -i key.pem ubuntu@ip`
3. Instalar Python 3.10
4. Clonar repositorio
5. Crear entorno virtual
6. Instalar dependencias
7. Entrenar modelo
8. Usar nginx como proxy inverso
9. Configurar SSL con certbot

#### Nginx Config:
```nginx
server {
    listen 80;
    server_name chatbot.unasam.edu.pe;

    location / {
        proxy_pass http://localhost:5005;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 7. **Google Cloud Platform**

#### Cloud Run:
```bash
gcloud run deploy unasam-chatbot \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

#### Dockerfile para Cloud Run:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN rasa train

EXPOSE 8080

ENV PORT=8080
CMD rasa run --enable-api --port $PORT --listen 0.0.0.0
```

### 8. **Microsoft Azure**

#### App Service:
```bash
az webapp up --name unasam-chatbot --resource-group myResourceGroup --runtime "PYTHON:3.10"
```

## 🔐 Seguridad en Producción

### Checklist:
- [ ] Usar HTTPS/TLS
- [ ] Validar autenticación
- [ ] Limitar tasa de requests (rate limiting)
- [ ] Encriptar datos sensibles
- [ ] Usar variables de entorno
- [ ] Configurar CORS correctamente
- [ ] Actualizar dependencias regularmente
- [ ] Implementar logging seguro
- [ ] Hacer backup de base de datos

### Variables de Entorno (.env):
```
RASA_API_KEY=your-secret-key
DATABASE_URL=postgresql://user:pass@host/db
TELEGRAM_TOKEN=your-token
SMTP_SERVER=mail.unasam.edu.pe
SMTP_USER=bot@unasam.edu.pe
SMTP_PASS=password
```

## 📊 Monitoreo

### Logs:
```bash
# Ver logs en tiempo real
docker logs -f unasam-chatbot

# Ver logs del sistema
journalctl -u unasam-chatbot -f
```

### Métricas:
- Número de conversaciones
- Tiempo de respuesta promedio
- Intenciones más consultadas
- Tasa de error
- Usuarios activos

## 🔄 CI/CD (GitHub Actions)

#### .github/workflows/deploy.yml:
```yaml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.10
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Train model
        run: rasa train
      - name: Run tests
        run: rasa test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Heroku
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{secrets.HEROKU_API_KEY}}
          heroku_app_name: "unasam-chatbot"
          heroku_email: ${{secrets.HEROKU_EMAIL}}
```

## 📈 Escalabilidad

### Recomendaciones:
- Usar Redis para caché de sesiones
- Implementar load balancer
- Usar microservicios para acciones
- Implementar queue (Celery)
- Usar CDN para assets
- Escalar horizontalmente con Kubernetes

## 🚀 Performance

### Optimizaciones:
- Comprimir modelo
- Usar GPU para inferencia
- Implementar caché de respuestas
- Usar async/await
- Implementar rate limiting
- Monitorear memory usage

---

**Más información**: Consulta README.md para detalles completos
