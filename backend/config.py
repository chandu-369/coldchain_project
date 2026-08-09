from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# MQTT Configuration
MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT"))

MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

MQTT_TOPIC = os.getenv("MQTT_TOPIC")