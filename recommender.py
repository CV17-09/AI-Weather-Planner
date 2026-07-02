def get_recommendation(weather):
    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind_speed"]
    condition = weather["condition"].lower()

    recommendations = []

    if "rain" in condition or "storm" in condition:
        recommendations.append("Carry an umbrella and avoid outdoor activities.")
    elif temp > 90:
        recommendations.append("It is very hot. Stay hydrated and avoid long outdoor exercise.")
    elif temp < 45:
        recommendations.append("Wear warm clothes if going outside.")
    else:
        recommendations.append("Good weather for walking, jogging, or visiting a park.")

    if humidity > 75:
        recommendations.append("Humidity is high, so outdoor exercise may feel harder.")

    if wind > 20:
        recommendations.append("Wind speed is high. Be careful with biking or outdoor events.")

    return recommendations