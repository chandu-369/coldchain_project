# ==========================================
# AI Prediction Engine
# ==========================================

def predict(history):

    # Not enough data yet
    if len(history) < 10:
        return {
            "trend": "COLLECTING DATA",
            "current": None,
            "predicted": None,
            "change": 0,
            "risk": "LOW",
            "minutes_to_breach": None
        }

    # Last 10 readings
    temps = [item["temperature"] for item in history[-10:]]

    first = temps[0]
    last = temps[-1]

    change = last - first

    # Trend
    if change > 2:
        trend = "RISING"

    elif change < -2:
        trend = "FALLING"

    else:
        trend = "STABLE"

    # Simple prediction
    predicted = last + (change * 3)

    # Risk calculation
    if predicted >= 25:
        risk = "CRITICAL"

    elif predicted >= 15:
        risk = "HIGH"

    elif predicted >= 8:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    # Estimated time until breach
    if change <= 0:
        minutes = None
    else:
        rate = change / 10
        remaining = 25 - last

        if remaining <= 0:
            minutes = 0
        else:
            minutes = round(remaining / rate)

    return {

        "trend": trend,

        "current": round(last,2),

        "predicted": round(predicted,2),

        "change": round(change,2),

        "risk": risk,

        "minutes_to_breach": minutes

    }