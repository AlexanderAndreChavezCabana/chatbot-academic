#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Custom Actions for UNASAM Chatbot
"""

from typing import Any, Text, Dict, List
from rasa_sdk import Action, FormValidationAction, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
import re
import json
import os
from datetime import datetime


class ValidateRegistroEstudianteForm(FormValidationAction):
    """Validates student registration form data"""

    def name(self) -> Text:
        return "validate_registro_estudiante_form"

    @staticmethod
    def validar_email(email: Text) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validar_telefono(telefono: Text) -> bool:
        """Validates phone number for Peru format"""
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
        pattern = r'^(\+51)?9\d{8}$'
        return re.match(pattern, telefono_limpio) is not None

    @staticmethod
    def validar_codigo_estudiante(codigo: Text) -> bool:
        """Validates student code format"""
        pattern = r'^\d{6,7}$'
        return re.match(pattern, codigo) is not None

    async def validate_nombre_usuario(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validates user name"""
        if slot_value and len(slot_value.strip()) > 2:
            return {"nombre_usuario": slot_value.strip()}
        else:
            dispatcher.utter_message(
                text="El nombre debe tener al menos 3 caracteres."
            )
            return {"nombre_usuario": None}

    async def validate_email_usuario(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validates email"""
        if slot_value and self.validar_email(slot_value):
            return {"email_usuario": slot_value.strip().lower()}
        else:
            dispatcher.utter_message(
                text="El correo electrónico no es válido."
            )
            return {"email_usuario": None}

    async def validate_telefono_usuario(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validates phone number"""
        if slot_value and self.validar_telefono(slot_value):
            telefono_limpio = re.sub(r'[\s\-\(\)]', '', slot_value)
            if not telefono_limpio.startswith('+51'):
                telefono_limpio = '+51' + telefono_limpio.lstrip('+51')
            return {"telefono_usuario": telefono_limpio}
        else:
            dispatcher.utter_message(
                text="El teléfono no es válido. Formato: 987654321"
            )
            return {"telefono_usuario": None}

    async def validate_codigo_estudiante(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validates student code"""
        if slot_value and self.validar_codigo_estudiante(slot_value):
            return {"codigo_estudiante": slot_value.strip()}
        else:
            dispatcher.utter_message(
                text="El código de estudiante debe tener 6-7 dígitos."
            )
            return {"codigo_estudiante": None}


class ActionRegistrarEstudiante(Action):
    """Registers student in the system"""

    def name(self) -> Text:
        return "action_registrar_estudiante"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        
        nombre = tracker.get_slot("nombre_usuario")
        email = tracker.get_slot("email_usuario")
        telefono = tracker.get_slot("telefono_usuario")
        codigo = tracker.get_slot("codigo_estudiante")
        
        # Create record
        registro = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nombre": nombre,
            "email": email,
            "telefono": telefono,
            "codigo_estudiante": codigo
        }
        
        # Save to JSON
        archivo = "estudiantes.json"
        registros = []
        
        if os.path.exists(archivo):
            try:
                with open(archivo, "r", encoding="utf-8") as f:
                    registros = json.load(f)
            except:
                registros = []
        
        registros.append(registro)
        
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(registros, f, ensure_ascii=False, indent=2)
        
        dispatcher.utter_message(
            text=f"✅ ¡Registro completado! Tu email: {email}"
        )
        
        return [SlotSet("registro_completado", True)]
