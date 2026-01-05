# 🚀 Guía de Inicio Rápido - Chatbot UNASAM

## ⚡ Instalación rápida (5 minutos)

### 1️⃣ Crear entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

*Esto puede tardar 10-15 minutos en la primera instalación*

### 3️⃣ Entrenar el modelo

```bash
rasa train
```

### 4️⃣ Ejecutar en otra terminal (el servidor de acciones)

```bash
rasa run actions
```

### 5️⃣ En otra terminal más, iniciar el chatbot

```bash
rasa shell
```

## ✅ Prueba tu chatbot

Una vez en la shell de RASA, escribe:

```
Tu: Hola
Bot: ¡Hola! Bienvenido a UNASAM. Soy tu asistente virtual académico. ¿En qué puedo ayudarte hoy?

Tu: ¿Qué carreras tienen?
Bot: 🎓 **Carreras Profesionales - UNASAM**
[Información de carreras]

Tu: Deseo inscribirse
Bot: [Inicia formulario de registro]
```

## 📚 Próximos pasos

1. Lee [README.md](README.md) para documentación completa
2. Modifica `domain.yml` para agregar más intenciones
3. Actualiza `data/nlu.yml` con más ejemplos de entrenamiento
4. Personaliza `actions/actions.py` con tu lógica custom

## 🔧 Comandos útiles

| Comando | Descripción |
|---------|-------------|
| `rasa train` | Entrenar modelo |
| `rasa shell` | Chatbot interactivo |
| `rasa run actions` | Servidor de acciones |
| `rasa test` | Ejecutar tests |
| `rasa run --enable-api` | Iniciar API REST |

## 📱 API REST (opcional)

Para usar el chatbot como API:

```bash
# Terminal 1 - Servidor de acciones
rasa run actions

# Terminal 2 - API REST
rasa run --enable-api --port 5005

# Terminal 3 - Test de API
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola"}'
```

## ⚠️ Solución de problemas

### Error: "No model found"
```bash
rasa train
```

### Error: "Action not found"
Asegúrate de que `rasa run actions` esté ejecutándose en otra terminal

### Puerto 5055 en uso
Cambia el puerto en `endpoints.yml`:
```yaml
action_endpoint:
  url: "http://localhost:5056/webhook"
```

## 📧 Contacto

- Email: info@unasam.edu.pe
- Teléfono: +51 (043) 422-6147
- Web: www.unasam.edu.pe

---

**¡Listo! Tu chatbot ya está funcionando. 🎉**
