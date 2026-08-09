import ssl
import json
import paho.mqtt.client as mqtt

from config import (
    MQTT_HOST,
    MQTT_PORT,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    MQTT_TOPIC,
)

import latest_data
import history

# ==========================================
# MQTT Connected
# ==========================================

def on_connect(client, userdata, flags, reason_code, properties=None):

    print("===================================")
    print("Connected to HiveMQ Cloud")
    print("Subscribed to Telemetry :", MQTT_TOPIC)

    client.subscribe(MQTT_TOPIC)

    # Driver alert topic
    client.subscribe("coldchain/driver")

    print("Subscribed to Driver Alerts : coldchain/driver")


# ==========================================
# MQTT Message Received
# ==========================================

def on_message(client, userdata, msg):

    try:

        topic = msg.topic
        payload = msg.payload.decode()

        print("\n===================================")
        print("Topic :", topic)
        print("Payload :", payload)
        print("===================================")

        # ----------------------------------
        # Driver Alert
        # ----------------------------------

        if topic == "coldchain/driver":

            print("Driver Command Received")
            print(payload)

            return

        # ----------------------------------
        # Telemetry
        # ----------------------------------

        data = json.loads(payload)

        latest_data.latest_data.clear()
        latest_data.latest_data.update(data)

        history.history.append(data.copy())

        if len(history.history) > 300:
            history.history.pop(0)

        print("Latest Telemetry Updated")
        print(latest_data.latest_data)

        print("History Size :", len(history.history))

    except Exception as e:

        print("MQTT Error :", e)


# ==========================================
# MQTT Client
# ==========================================

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.username_pw_set(
    MQTT_USERNAME,
    MQTT_PASSWORD
)

client.tls_set(
    tls_version=ssl.PROTOCOL_TLS_CLIENT
)

client.on_connect = on_connect
client.on_message = on_message


# ==========================================
# Start MQTT
# ==========================================

def start_mqtt():

    print("Connecting to HiveMQ...")

    client.connect(
        MQTT_HOST,
        MQTT_PORT,
        60
    )

    client.loop_start()
# ==========================================
# Publish Message
# ==========================================

def publish_message(topic, message):

    client.publish(topic, message)

    print("===================================")
    print("Topic :", topic)
    print("Payload :", message)
    print("===================================")