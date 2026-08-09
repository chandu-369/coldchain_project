# Autonomous Cold-Chain Integrity & Rerouting

An IoT-based cold-chain monitoring prototype for monitoring temperature, humidity and vehicle location, predicting cold-chain risk, recommending nearby cold-storage facilities, obtaining owner reroute approval and sending driver alerts through Telegram.

## Technologies

- ESP32
- Wokwi
- MQTT
- HiveMQ Cloud
- FastAPI
- Python
- React
- Vite
- Telegram Bot API

## System Flow

ESP32/Wokwi → MQTT → HiveMQ Cloud → FastAPI Backend → React Dashboard

AI Prediction → Route Recommendation → Owner Approval → Driver Alert

## Project Status

Prototype / Demonstration
## System Architecture

![System Architecture](docs/system-overview.png)
## Demonstration

### Wokwi + ESP32 Simulation
![Wokwi ESP32](docs/screenshots/WokwiwithESP32.png)

### HiveMQ Cloud
![HiveMQ Cloud](docs/screenshots/HiveMQ.png)

### Safe Condition
![Safe Condition](docs/screenshots/Safe.png)

### Warning Condition
![Warning Condition](docs/screenshots/Warning.png)

### High Temperature Alert
![High Temperature](docs/screenshots/HighTemperature.png)

### Owner Approval
![Owner Approval](docs/screenshots/ApproveMessage.png)

### Route Rejection
![Route Rejection](docs/screenshots/Rejectmessage.png)
