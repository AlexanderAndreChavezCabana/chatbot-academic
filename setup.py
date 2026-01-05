"""
Setup script - Chatbot Académico UNASAM
"""

import os
import sys
import subprocess

def crear_directorios():
    directorios = ['models', 'data_usuarios', 'data_usuarios/logs']
    for directorio in directorios:
        if not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f"✓ Directorio creado: {directorio}")

def instalar_dependencias():
    print("\n📦 Instalando dependencias...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def entrenar_modelo():
    print("\n🧠 Entrenando modelo...")
    respuesta = input("¿Deseas entrenar el modelo ahora? (s/n): ")
    if respuesta.lower() == 's':
        subprocess.run(['rasa', 'train'])
        print("✓ Modelo entrenado exitosamente")
    else:
        print("⏭️  Salta al siguiente paso")

def mostrar_siguientes_pasos():
    print("\n" + "="*60)
    print("✅ INSTALACIÓN COMPLETADA")
    print("="*60)
    print("\n🚀 Próximos pasos:")
    print("\n1. En Terminal 1 - Ejecutar servidor de acciones:")
    print("   rasa run actions")
    print("\n2. En Terminal 2 - Ejecutar el chatbot:")
    print("   rasa shell")
    print("\n3. ¡Empieza a conversar con el chatbot!")
    print("\n📖 Más información en:")
    print("   - README.md")
    print("   - INICIO_RAPIDO.md")
    print("   - COMPARACION_CHATBOTS.md")
    print("\n" + "="*60)

def main():
    print("="*60)
    print("🎓 CHATBOT ACADÉMICO UNASAM - INSTALACIÓN")
    print("="*60)
    crear_directorios()
    instalar_dependencias()
    entrenar_modelo()
    mostrar_siguientes_pasos()

if __name__ == '__main__':
    main()
