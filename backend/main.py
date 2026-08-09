from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mqtt_client import (
    start_mqtt,
    publish_message
)


import latest_data
import history
import reroute
from route_ai import find_best_route
from telegram_alert import send_telegram
from datetime import datetime, timedelta
app = FastAPI(title="Cold Chain Backend")

# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

# ==========================================
# MQTT Startup
# ==========================================

@app.on_event("startup")
def startup():

    print("=" * 40)
    print("Starting Backend")
    print("=" * 40)

    start_mqtt()


# ==========================================
# Home
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Cold Chain Backend Running"
    }


# ==========================================
# Health
# ==========================================

@app.get("/health")
def health():

    return {
        "status": "Backend Running"
    }


# ==========================================
# Latest Telemetry
# ==========================================

@app.get("/telemetry/latest")
def latest():

    return latest_data.latest_data


# ==========================================
# Telemetry History
# ==========================================

@app.get("/telemetry/history")
def telemetry_history():

    return history.history


# ==========================================
# AI Prediction
# ==========================================

@app.get("/prediction")
def prediction():

    data = history.history

    if len(data) < 5:

        return {

            "trend": "COLLECTING DATA",
            "current": None,
            "predicted": None,
            "change": 0,
            "risk": "LOW",
            "minutes_to_breach": None

        }

    temperatures = []

    for item in data[-5:]:

        temperatures.append(item["temperature"])

    current = temperatures[-1]

    avg_change = (
        temperatures[-1] - temperatures[0]
    ) / 4

    predicted = current + avg_change * 30

    change = predicted - current

    if avg_change > 0:
        trend = "RISING"

    elif avg_change < 0:
        trend = "FALLING"

    else:
        trend = "STABLE"

    if predicted <= 8:

        risk = "LOW"
        minutes = None

    elif predicted <= 12:

        risk = "MEDIUM"
        minutes = 30

    else:

        risk = "HIGH"
        minutes = 15

    return {

        "trend": trend,
        "current": round(current,2),
        "predicted": round(predicted,2),
        "change": round(change,2),
        "risk": risk,
        "minutes_to_breach": minutes

    }


# ==========================================
# Current Reroute Status
# ==========================================

@app.get("/reroute")
def reroute_status():

    return reroute.reroute


# ==========================================
# Publish MQTT Helper
# ==========================================




# ==========================================
# Owner Approves
# ==========================================
@app.post("/reroute/approve")
def approve():

    reroute.reroute["approved"] = True
    reroute.reroute["message"] = "Owner Approved Reroute"

    # Send MQTT command to ESP32
    publish_message(
        "coldchain/driver",
        "APPROVED"
    )

    # Get latest telemetry
    telemetry = latest_data.latest_data

    # Get prediction
    prediction_data = prediction()

    # Get recommended route
    route_data = route()

    # Calculate estimated breach time
    breach_time = "Unknown"

    if prediction_data["minutes_to_breach"] is not None:

        breach_time = (
            datetime.now() +
            timedelta(
                minutes=prediction_data["minutes_to_breach"]
            )
        ).strftime("%I:%M %p")

    # Build Telegram message
    message = f"""
🚨 COLD CHAIN ALERT

Vehicle : {telemetry.get("vehicleId")}

Medicine : {telemetry.get("medicine")}

✅ OWNER APPROVED REROUTE

📍 Destination
{route_data.get("destination")}

🛣 Distance
{route_data.get("distance")} km

🚗 ETA
{route_data.get("eta")} Minutes

🌡 Current Temperature
{telemetry.get("temperature")} °C

📈 Temperature Trend
{prediction_data.get("trend")}

⏳ Safe Time Remaining
{prediction_data.get("minutes_to_breach")} Minutes

⚠ Estimated Cold-Chain Breach
{breach_time}

➡ Proceed immediately to the nearest cold storage.
"""

    send_telegram(message)

    print("Published -> APPROVED")

    return reroute.reroute

# ==========================================
# Owner Rejects
# ==========================================

@app.post("/reroute/reject")
def reject():

    reroute.reroute["approved"] = False
    reroute.reroute["message"] = "Owner Rejected Reroute"

    # Send MQTT command to ESP32
    publish_message(
        "coldchain/driver",
        "REJECTED"
    )

    # Get latest telemetry
    telemetry = latest_data.latest_data

    # Get prediction
    prediction_data = prediction()

    # Build Telegram message
    message = f"""
🚨 COLD CHAIN ALERT

Vehicle : {telemetry.get("vehicleId")}

Medicine : {telemetry.get("medicine")}

❌ OWNER REJECTED REROUTE

🌡 Current Temperature
{telemetry.get("temperature")} °C

📈 Temperature Trend
{prediction_data.get("trend")}

⚠ Continue on Current Route

Please monitor the cold chain carefully.
"""

    send_telegram(message)

    print("Published -> REJECTED")

    return reroute.reroute
# ==========================================
# AI Route Recommendation
# ==========================================

@app.get("/route")
def route():

    if not latest_data.latest_data:

        return {
            "destination": None,
            "distance": None,
            "eta": None
        }

    current_lat = latest_data.latest_data["latitude"]
    current_lon = latest_data.latest_data["longitude"]

    return find_best_route(
        current_lat,
        current_lon

    )