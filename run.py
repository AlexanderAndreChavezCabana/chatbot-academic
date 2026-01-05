"""
Script para iniciar el chatbot UNASAM
"""

import subprocess
import sys
from threading import Thread
import time

def ejecutar_servidor_acciones():
    print("🚀 Iniciando servidor de acciones (puerto 5055)...")
    subprocess.run(['rasa', 'run', 'actions'])

def ejecutar_chatbot():
    print("💬 Iniciando chatbot UNASAM...")
    time.sleep(3)
    subprocess.run(['rasa', 'shell'])

def main():
    print("="*60)
    print("🎓 CHATBOT ACADÉMICO UNASAM")
    print("="*60)
    print("\n⚠️  Este script abrirá dos procesos:")
    print("   1. Servidor de acciones (puerto 5055)")
    print("   2. Chatbot interactivo (shell)")
    print("\nPara detener, presiona Ctrl+C")
    print("="*60 + "\n")
    
    thread_acciones = Thread(target=ejecutar_servidor_acciones, daemon=True)
    thread_acciones.start()
    
    time.sleep(2)
    ejecutar_chatbot()

if __name__ == '__main__':
    main()
