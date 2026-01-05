#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom Actions - Chatbot UNASAM
"""

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
import re
import json
import os
from datetime import datetime
import random
import sqlite3


class ValidateRegistroEstudianteForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_registro_estudiante_form"

    @staticmethod
    def validar_email(email: Text) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validar_telefono(telefono: Text) -> bool:
        """Valida que el teléfono tenga formato correcto (Perú)"""
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
        pattern = r'^(\+51)?9\d{8}$'
        return re.match(pattern, telefono_limpio) is not None

    @staticmethod
    def validar_codigo_estudiante(codigo: Text) -> bool:
        """Valida que el código de estudiante tenga formato correcto"""
        # Formato: 6-7 dígitos, ejemplo: 2024001
        pattern = r'^\d{6,7}$'
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
        pattern = r'^(\+51)?9\d{8}$'
        return re.match(pattern, telefono_limpio) is not None

    @staticmethod
    def validar_codigo_estudiante(codigo: Text) -> bool:
        pattern = r'^\d{6,7}$'
        return re.match(pattern, codigo) is not None

    async def validate_nombre_usuario(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valida el email del usuario"""

        if slot_value and self.validar_email(slot_value):
            return {"email_usuario": slot_value.strip().lower()}
        else:
            )
            return {"email_usuario": None}

    async def validate_telefono_usuario(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valida el teléfono del usuario"""

        if slot_value and self.validar_telefono(slot_value):
            telefono_limpio = re.sub(r'[\s\-\(\)]', '', slot_value)
            if not telefono_limpio.startswith('+51'):
                telefono_limpio = '+51' + telefono_limpio.lstrip('+51')
            return {"telefono_usuario": telefono_limpio}
                text="El teléfono no es válido. Por favor, ingresa un número de celular peruano (9 dígitos)"
            )
            return {"telefono_usuario": None}

    async def validate_codigo_estudiante(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Valida el código de estudiante"""

        if slot_value and self.validar_codigo_estudiante(slot_value):
            return {"codigo_estudiante": slot_value.strip()}
                text="El código de estudiante no es válido. Por favor, verifica tu código (ejemplo: 2024001)"
            )
            return {"codigo_estudiante": None}


class ActionRegistrarEstudiante(Action):
    """Acción para registrar al estudiante en la base de datos"""

    def name(self) -> Text:
        return "action_registrar_estudiante"

    def _crear_base_datos(self) -> str:

    def name(self) -> Text:
        return "action_registrar_estudiante"

    def _crear_base_datos(self) -> str:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE estudiantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id TEXT UNIQUE NOT NULL,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    telefono TEXT NOT NULL,
                    codigo_estudiante TEXT UNIQUE NOT NULL,
                    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    estado TEXT DEFAULT 'activo'
                )
            ''')
            
            conn.commit()
            conn.close()
        
        return db_path

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Ejecuta el registro del estudiante"""

        # Obtener datos de los slots
        nombre = tracker.get_slot("nombre_usuario")
        email = tracker.get_slot("email_usuario")
        telefono = tracker.get_slot("telefono_usuario")
        nombre = tracker.get_slot("nombre_usuario")
        email = tracker.get_slot("email_usuario")
        telefono = tracker.get_slot("telefono_usuario")
        codigo_estudiante = tracker.get_slot("codigo_estudiante")

        db_path = self._crear_base_datos()
            
            cursor.execute('''
                INSERT INTO estudiantes (student_id, nombre, email, telefono, codigo_estudiante)
                VALUES (?, ?, ?, ?, ?)
            ''', (student_id, nombre, email, telefono, codigo_estudiante))
            
            conn.commit()
            conn.close()
            
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO estudiantes (student_id, nombre, email, telefono, codigo_estudiante)
                VALUES (?, ?, ?, ?, ?)
            ''', (student_id, nombre, email, telefono, codigo_estudiante))
            
            conn.commit()
            conn.close()
            
            data_dir = os.path.join(os.path.dirname(__file__), '..', 'data_usuarios')ding='utf-8') as f:
                json.dump(estudiante_data, f, indent=2, ensure_ascii=False)
            
            # Mensaje de confirmación
            dispatcher.utter_message(
                text=f"¡Excelente {nombre}! Tu registro ha sido completado exitosamente.\n\n"
                     f"📋 Datos registrados:\n"
                     f"• ID de estudiante: {student_id}\n"
                     f"• Correo: {email}\n"
                     f"• Teléfono: {telefono}\n"
                     f"• Código: {codigo_estudiante}\n\n"
                     f"Pronto recibirás un correo de confirmación con tu información."
            )
            
            return [SlotSet("registro_completado", True)]
            
        except sqlite3.IntegrityError as e:
                text="Lo siento, parece que ya existe un registro con ese email o código de estudiante. "
                     "Por favor, contacta a registro@unasam.edu.pe"
            )
            return [SlotSet("registro_completado", False)]
        except Exception as e:
            dispatcher.utter_message(
                text=f"Ocurrió un error durante el registro: {str(e)}. "
                     "Por favor, intenta de nuevo o contacta a soporte."
            )
            return [SlotSet("registro_completado", False)]


class ActionGuardarConversacion(Action):
    """Acción para guardar la conversación en logs"""

    def name(self) -> Text:
        return "action_guardar_conversacion"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Guarda la conversación actual"""

        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data_usuarios', 'logs')
        os.makedirs(data_dir, exist_ok=True)

    def name(self) -> Text:
        return "action_guardar_conversacion"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        try:
            with open(archivo_log, 'w', encoding='utf-8') as f:
                json.dump(conversation_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error al guardar conversación: {str(e)}")
return []


class ActionConsultarCarrera(Action):
    """Acción para consultar información de carreras"""

    def name(self) -> Text:
        return "action_consultar_carrera"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        """Proporciona información de carreras"""

        carreras_unasam = {
            "ingenieria_sistemas": {
                "nombre": "Ingeniería de Sistemas",

    def name(self) -> Text:
        return "action_consultar_carrera"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
            "administracion": {
                "nombre": "Administración",
                "facultad": "Facultad de Administración",
                "duracion": "4 años",
                "creditos": 170,
                "modalidad": "Presencial"
            }
        }

        return []
