"""
Configuracion - Chatbot Académico UNASAM
"""

import os

DEBUG = True
ENVIRONMENT = 'development'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data_usuarios')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
LOGS_DIR = os.path.join(DATA_DIR, 'logs')

RASA_MODEL_PATH = os.path.join(MODELS_DIR, 'latest')
RASA_ACTIONS_ENDPOINT = 'http://localhost:5055/webhook'

DATABASE_PATH = os.path.join(DATA_DIR, 'estudiantes.db')
DATABASE_TYPE = 'sqlite'

API_HOST = 'localhost'
API_PORT = 5005
API_DEBUG = True

LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

CHATBOT_NAME = 'UNASAM Bot'
CHATBOT_LANGUAGE = 'es'
CHATBOT_TIMEZONE = 'America/Lima'

UNIVERSITY_NAME = 'Universidad Nacional Santiago Antúnez de Mayolo'
UNIVERSITY_LOCATION = 'Huaraz, Ancash - Perú'
UNIVERSITY_CONTACT = '+51 (043) 422-6147'
UNIVERSITY_EMAIL = 'info@unasam.edu.pe'
UNIVERSITY_WEBSITE = 'www.unasam.edu.pe'

ENABLE_EMAIL_NOTIFICATIONS = False
ENABLE_SMS_NOTIFICATIONS = False
ENABLE_ANALYTICS = True
ENABLE_LOGGING = True

VALIDATE_EMAIL = True
VALIDATE_PHONE = True
VALIDATE_STUDENT_CODE = True
