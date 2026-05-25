"""
Módulo de Automatización del Pipeline de Abastecimiento

Este script programa la ejecución automática del modelo
en horarios específicos, simulando un orquestador de pipelines.

Autor: [Tu Nombre]
Fecha: Mayo 2026
"""

import schedule
import time
import logging
from datetime import datetime
from abastecimiento import main as ejecutar_modelo

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/pipeline.log'),
        logging.StreamHandler()
    ]
)

def ejecutar_con_logging():
    """Ejecuta el modelo con registro de logs"""
    logging.info("🚀 Iniciando ejecución del modelo de abastecimiento")
    try:
        ejecutar_modelo()
        logging.info("✅ Ejecución completada exitosamente")
    except Exception as e:
        logging.error(f"❌ Error en la ejecución: {str(e)}")

# Programación de ejecuciones
schedule.every().day.at("06:00").do(ejecutar_con_logging)      # Diario a las 6 AM
schedule.every().monday.at("06:00").do(ejecutar_con_logging)   # Especial los lunes
schedule.every().day.at("14:00").do(ejecutar_con_logging)      # Refuerzo vespertino

# Ejecutar inmediatamente al inicio (para pruebas)
ejecutar_con_logging()

logging.info("📅 Scheduler iniciado. Esperando tareas programadas...")
logging.info("   - Ejecución diaria: 6:00 AM y 2:00 PM")
logging.info("   - Ejecución especial: lunes a las 6:00 AM")

try:
    while True:
        schedule.run_pending()
        time.sleep(60)  # Revisar cada minuto
except KeyboardInterrupt:
    logging.info("🛑 Scheduler detenido por el usuario")