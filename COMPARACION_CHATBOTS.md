# Estructura del Proyecto Chatbot UNASAM

## 📊 Comparación de Herramientas de Chatbots

### RASA vs Alternativas

| Característica | RASA | Dialogflow | Botpress | LangChain |
|---------------|------|-----------|----------|-----------|
| **Open Source** | ✅ Sí | ❌ No | ✅ Sí | ✅ Sí |
| **Costo** | Gratis | Pago | Freemium | Gratis |
| **Complejidad** | Media-Alta | Baja | Media | Alta |
| **NLU Integrado** | ✅ Sí | ✅ Sí | ✅ Sí | ❌ No |
| **Personalización** | ✅ Alta | ❌ Limitada | ✅ Media | ✅ Alta |
| **Curva aprendizaje** | 📈 Media | 📉 Baja | 📈 Media | 📈 Alta |
| **Deploy** | ✅ Flexible | ☁️ Cloud | ☁️ Cloud | ✅ Flexible |

## 🏗️ Arquitectura de RASA

```
┌─────────────────────────────────────────────────┐
│           Entrada de Usuario                    │
│         (texto natural)                         │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│          NLU Pipeline                           │
│  • Tokenización                                 │
│  • Extracción de características                │
│  • Clasificación de intenciones                 │
│  • Extracción de entidades                      │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│          Dialog Manager (Core)                  │
│  • Políticas de diálogo                        │
│  • Historias de conversación                    │
│  • Seguimiento de estado (slots)                │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│          Policy Selection                       │
│  • MemoizationPolicy                           │
│  • RulePolicy                                   │
│  • TEDPolicy                                    │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│          Action Selection                       │
│  • Respuestas predefinidas (utter_*)           │
│  • Acciones custom (action_*)                   │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│        Response Action Executor                 │
│   (action_endpoint - localhost:5055)            │
└────────────┬────────────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────┐
│         Respuesta al Usuario                    │
└─────────────────────────────────────────────────┘
```

## 📂 Desglose de Carpetas

```
chatbot-academic/
├── data/                          # Datos de entrenamiento
│   ├── nlu.yml                   # Intenciones y ejemplos (591 líneas)
│   ├── stories.yml               # Historias de diálogo
│   └── rules.yml                 # Reglas determinísticas
│
├── actions/                       # Acciones custom
│   ├── __init__.py
│   └── actions.py                # Lógica personalizada
│
├── config.yml                     # Configuración del pipeline NLU
├── domain.yml                     # Dominio (intenciones, slots, respuestas)
├── credentials.yml                # Credenciales de conectores
├── endpoints.yml                  # Endpoints de servicios
├── requirements.txt               # Dependencias Python
├── README.md                      # Documentación principal
├── INICIO_RAPIDO.md              # Guía de inicio
├── COMPARACION_CHATBOTS.md       # Este archivo
├── models/                        # Modelos entrenados
├── data_usuarios/                 # Base de datos de usuarios
└── tests/                         # Tests de historias
    └── test_stories.yml
```

## 🧠 Componentes de RASA

### 1. **NLU (Natural Language Understanding)**
- Entiende la intención del usuario
- Extrae entidades relevantes
- Basado en machine learning

**Archivo**: `data/nlu.yml`
- 13 intenciones principales
- 591 ejemplos de entrenamiento

### 2. **Dialog Management (Core)**
- Decide qué acción tomar
- Mantiene el estado de la conversación
- Usa políticas de diálogo

**Archivos**:
- `data/stories.yml` - Historias de diálogo
- `data/rules.yml` - Reglas determinísticas
- `domain.yml` - Configuración del dominio

### 3. **Actions**
- Responden al usuario
- Implementan lógica custom

**Archivo**: `actions/actions.py`
- ValidateRegistroEstudianteForm
- ActionRegistrarEstudiante
- ActionGuardarConversacion
- ActionConsultarCarrera

### 4. **Policies**
Determinan qué acción ejecutar:

- **MemoizationPolicy**: Memoriza conversaciones exactas
- **RulePolicy**: Aplica reglas predefinidas
- **TEDPolicy**: Usa transformer para predicciones

## 📊 Estadísticas del Proyecto

| Métrica | Cantidad |
|---------|----------|
| Intenciones | 34 |
| Entidades | 6 |
| Slots | 9 |
| Ejemplos NLU | 591 |
| Historias | 20 |
| Respuestas | 24 |
| Acciones custom | 4 |
| Líneas de código Python | 397+ |

## 🔄 Flujo de Entrenamiento

```
datos/nlu.yml
     │
     ▼
Tokenización
     │
     ▼
Extracción de características
     │
     ▼
DIETClassifier (entrenamiento)
     │
     ▼
Modelo NLU entrenado
     │
     ├─────────────────────────┐
     │                         │
     ▼                         ▼
datos/stories.yml      Políticas
     │                         │
     ▼                         ▼
     └─────────────────────────┘
              │
              ▼
        Modelo Dialog Manager
              │
              ▼
      Model.tar.gz (guardado)
```

## 🎯 Intenciones por Categoría

### Generales (5)
- saludo, despedida, afirmar, negar, agradecer

### Académicas Generales (5)
- consultar_carrera, consultar_facultad, consultar_contacto, consultar_ubicacion, consultar_historia_universidad

### Horarios y Calendarios (4)
- consultar_horario_clase, consultar_calendario_academico, consultar_fechas_examen, consultar_periodo_matricula

### Cursos y Docentes (4)
- consultar_docente, consultar_silabo_curso, consultar_calificaciones, consultar_asistencia

### Servicios (5)
- consultar_biblioteca, consultar_becas, consultar_tramites, solicitar_constancia_estudiante, consultar_creditos

### Registro (8)
- deseo_inscribirse, proporcionar_nombre, proporcionar_email, proporcionar_telefono, proporcionar_codigo_estudiante, confirmar_datos, consultar_metodos_pago, confirmar_pago

### Soporte (2)
- error_general, contacto_soporte, solicitar_asesor_academico

## 🗄️ Base de Datos

### SQLite (`data_usuarios/estudiantes.db`)
```sql
CREATE TABLE estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT UNIQUE NOT NULL,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefono TEXT NOT NULL,
    codigo_estudiante TEXT UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado TEXT DEFAULT 'activo'
);
```

### JSON (`data_usuarios/STU_*.json`)
```json
{
  "student_id": "STU_20240105_120530_5234",
  "nombre": "Juan Pérez",
  "email": "juan@unasam.edu.pe",
  "telefono": "+51987654321",
  "codigo_estudiante": "2024001",
  "fecha_registro": "2024-01-05T12:05:30.123456",
  "estado": "registrado"
}
```

## 🚀 Ventajas de esta Implementación

✅ **Open Source** - Sin costos de licencia
✅ **Flexible** - Personalizable completamente
✅ **Escalable** - Puede crecer sin problemas
✅ **Local** - Se ejecuta en tu máquina
✅ **Integrable** - API REST disponible
✅ **Seguro** - Control total de datos
✅ **Documentado** - Código bien comentado

## 🔮 Mejoras Futuras

- [ ] Integración con Telegram
- [ ] Integración con WhatsApp
- [ ] Análisis de sentimientos
- [ ] Recomendaciones inteligentes
- [ ] Chat en tiempo real en web
- [ ] Analytics y reportes
- [ ] Integración con calendario (Google Calendar)
- [ ] Envío de emails automático

---

**Versión**: 1.0
**Última actualización**: Enero 2026
