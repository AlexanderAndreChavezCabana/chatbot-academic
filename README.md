# Chatbot Académico UNASAM

**Asistente Virtual de la Universidad Nacional Santiago Antúnez de Mayolo**

## 📋 Descripción

Chatbot desarrollado con **RASA** para proporcionar soporte académico a estudiantes, docentes y público en general de la Universidad Nacional Santiago Antúnez de Mayolo (UNASAM).

### Funcionalidades principales:

✅ **Información General**
- Historia y ubicación de UNASAM
- Facultades y carreras disponibles
- Contacto y horarios de atención

✅ **Soporte Académico**
- Consultas de horarios de clases
- Calendario académico y fechas de examen
- Información sobre docentes
- Sílabos de cursos
- Consulta de calificaciones y asistencia

✅ **Servicios Estudiantiles**
- Sistema de becas
- Acceso a biblioteca
- Información de trámites
- Constancia de estudiante
- Sistema de créditos

✅ **Registro y Matrícula**
- Formulario de registro de estudiantes
- Información de métodos de pago
- Validación de datos

## 🛠️ Tecnología

- **Framework**: RASA 3.6.3+
- **Lenguaje**: Python 3.10+
- **NLU**: Español (es)
- **Base de Datos**: SQLite + JSON

## 📁 Estructura del Proyecto

```
chatbot-academic/
├── data/
│   ├── nlu.yml           # Intenciones y ejemplos
│   ├── stories.yml       # Historias de conversación
│   └── rules.yml         # Reglas del chatbot
├── actions/
│   ├── __init__.py
│   └── actions.py        # Acciones personalizadas
├── config.yml            # Configuración de RASA
├── domain.yml            # Dominio del chatbot
├── credentials.yml       # Credenciales
├── endpoints.yml         # Endpoints
├── requirements.txt      # Dependencias
└── README.md            # Este archivo
```

## ⚙️ Instalación

### 1. Crear entorno virtual

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

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Entrenar el modelo

```bash
rasa train
```

### 4. Ejecutar el servidor de acciones (en otra terminal)

```bash
rasa run actions
```

### 5. Iniciar el chatbot (en otra terminal)

**Modo interactivo:**
```bash
rasa shell
```

**Servidor API:**
```bash
rasa run --enable-api --port 5005
```

## 🚀 Uso

### Modo Interactivo

```bash
rasa shell
```

Ejemplo de conversación:
```
Tu: Hola
Bot: ¡Hola! Bienvenido a UNASAM. Soy tu asistente virtual académico. ¿En qué puedo ayudarte hoy?

Tu: ¿Qué carreras ofrecen?
Bot: [Información de carreras disponibles]

Tu: Deseo inscribirse
Bot: [Inicia formulario de registro]
```

### API REST

El chatbot también funciona como servidor API:

```bash
# Iniciar servidor
rasa run --enable-api --port 5005

# En otra terminal, hacer consulta:
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola"}'
```

## 📊 Intenciones Disponibles

### Generales
- `saludo` - Saludar al chatbot
- `despedida` - Despedirse
- `agradecer` - Agradecer

### Información Académica
- `consultar_carrera` - Información de carreras
- `consultar_facultad` - Facultades disponibles
- `consultar_historia_universidad` - Historia de UNASAM
- `consultar_ubicacion` - Ubicación y contacto

### Horarios y Calendarios
- `consultar_horario_clase` - Horarios de clases
- `consultar_calendario_academico` - Calendario académico
- `consultar_fechas_examen` - Fechas de examen
- `consultar_periodo_matricula` - Período de matrícula

### Servicios
- `consultar_biblioteca` - Información de biblioteca
- `consultar_becas` - Sistema de becas
- `consultar_tramites` - Trámites académicos
- `solicitar_constancia_estudiante` - Constancia de estudiante

### Registro
- `deseo_inscribirse` - Desea registrarse
- `proporcionar_nombre`, `proporcionar_email`, `proporcionar_telefono`, `proporcionar_codigo_estudiante`

## 🗄️ Base de Datos

### SQLite
Los registros de estudiantes se guardan en:
```
data_usuarios/estudiantes.db
```

Estructura de tabla:
```sql
CREATE TABLE estudiantes (
    id INTEGER PRIMARY KEY,
    student_id TEXT UNIQUE,
    nombre TEXT,
    email TEXT UNIQUE,
    telefono TEXT,
    codigo_estudiante TEXT UNIQUE,
    fecha_registro TIMESTAMP,
    estado TEXT
);
```

### JSON
Respaldo en:
```
data_usuarios/STU_*.json
```

## 🧪 Testing

Ejecutar tests de historias:

```bash
rasa test
```

## 📝 Configuración del NLU

El pipeline utiliza:
- **WhitespaceTokenizer** - Tokenización
- **RegexFeaturizer** - Características regex
- **LexicalSyntacticFeaturizer** - Características sintácticas
- **CountVectorsFeaturizer** - Vectorización
- **DIETClassifier** - Clasificación de intenciones y entidades
- **ResponseSelector** - Selección de respuestas
- **FallbackClassifier** - Manejo de consultas no entendidas

## 🔐 Seguridad

- Las contraseñas nunca se almacenan
- Los datos de estudiantes se guardan en SQLite con respaldo JSON
- Se validan todos los inputs (email, teléfono, código)

## 🐛 Troubleshooting

### Error: "No model found"
```bash
rasa train
```

### Error: "Action not found"
Asegúrate de que `action_endpoint` esté ejecutándose:
```bash
rasa run actions
```

### Error de conexión a acciones
Verifica que el puerto 5055 esté disponible

## 📧 Contacto y Soporte

Para problemas o sugerencias:
- Email: info@unasam.edu.pe
- Teléfono: +51 (043) 422-6147
- Portal: www.unasam.edu.pe

## 📄 Licencia

Este proyecto es propiedad de la Universidad Nacional Santiago Antúnez de Mayolo (UNASAM).

## 👥 Desarrollo

Desarrollado para mejorar la experiencia académica de estudiantes de UNASAM.

---

**Última actualización**: Enero 2026
**Versión**: 1.0
