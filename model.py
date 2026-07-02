def predict_activity_suitability(weather):
    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind_speed"]
    condition = weather["condition"].lower()

    if "storm" in condition or "rain" in condition:
        return "Poor"
    if temp > 95 or temp < 35:
        return "Poor"
    if humidity > 85 or wind > 25:
        return "Moderate"

    return "Good"