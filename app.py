import streamlit as st
from weather_api import get_weather
from recommender import get_recommendation
from model import predict_activity_suitability

st.set_page_config(page_title="AI Weather Planner", page_icon="🌤️")

st.title("AI Weather Planner")
st.write("Get real-time weather and AI-powered activity recommendations.")

city = st.text_input("Enter a city", "Houston")

if st.button("Get Weather Plan"):
    weather = get_weather(city)

    if weather is None:
        st.error("Could not find weather for that city.")
    else:
        st.subheader(f"Current Weather in {weather['city']}")

        st.metric("Temperature", f"{weather['temperature']} °F")
        st.metric("Humidity", f"{weather['humidity']}%")
        st.metric("Wind Speed", f"{weather['wind_speed']} mph")
        st.write(f"Condition: {weather['condition']}")

        suitability = predict_activity_suitability(weather)
        st.subheader("Outdoor Activity Suitability")
        st.write(suitability)

        st.subheader("AI Recommendations")
        recommendations = get_recommendation(weather)

        for rec in recommendations:
            st.write(f"- {rec}")