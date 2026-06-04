# AI Weather Planner 🌤️🤖

AI Weather Planner is an intelligent weather assistant that combines real-time weather forecasting, predictive analytics, and AI-generated recommendations to help users plan their day.

The application retrieves live weather data, analyzes environmental conditions such as temperature, humidity, wind speed, and precipitation, and provides personalized activity suggestions. Whether users are planning outdoor activities, exercise, travel, or simply deciding what to wear, AI Weather Planner offers data-driven recommendations based on current and forecasted weather conditions.

---

## Features

### Real-Time Weather Forecasts
- Retrieve current weather information for any city.
- Display temperature, humidity, wind speed, and weather conditions.
- Access short-term weather forecasts.

### AI-Powered Activity Recommendations
- Suggest outdoor or indoor activities based on weather conditions.
- Recommend actions such as:
  - Going for a walk
  - Running outdoors
  - Visiting a park
  - Carrying an umbrella
  - Staying indoors during severe weather

### Predictive Weather Analysis
- Analyze weather trends and forecast conditions.
- Predict the suitability of outdoor activities.
- Generate weather-based planning suggestions.

### User-Friendly Interface
- Simple and intuitive web application.
- Easy city search functionality.
- Responsive design for desktop and mobile devices.

---

## Technologies Used

### Programming Language
- Python

### Libraries and Frameworks
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Requests

### APIs
- OpenWeatherMap API

### Version Control
- Git
- GitHub

---

## Project Structure

```text
ai-weather-planner/
│
├── app.py
├── weather_api.py
├── recommender.py
├── model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sample_weather_data.csv
│
├── screenshots/
│
└── .env
```

---

## How It Works

1. User enters a city name.
2. The application retrieves real-time weather data from the OpenWeatherMap API.
3. Weather conditions are processed and analyzed.
4. A predictive model evaluates weather suitability for various activities.
5. The AI recommendation engine generates personalized suggestions.
6. Results are displayed through the web interface.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/ai-weather-planner.git
cd ai-weather-planner
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

You can obtain a free API key from OpenWeatherMap.

---

## Running the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## Example Output

### Current Weather

```text
Location: Houston, TX
Temperature: 85°F
Humidity: 70%
Wind Speed: 10 mph
Condition: Partly Cloudy
```

### AI Recommendation

```text
Great weather for outdoor activities.
Consider going for a walk, jogging, or visiting a local park.
Bring water and sunscreen due to high temperatures.
```

---

## Future Enhancements

- User profiles and preferences
- Weather alerts and notifications
- 7-day forecast visualization
- Machine learning forecast optimization
- Voice assistant integration
- Mobile application support
- LLM-powered conversational weather chatbot

---

## Learning Objectives

This project demonstrates:

- API integration
- Data collection and preprocessing
- Predictive modeling
- AI-assisted recommendations
- Web application development
- Real-time data analysis
- Software engineering best practices

---

## Author

Claudia Dominguez

Computer Science Student | Data Science Minor

Interested in Artificial Intelligence, Machine Learning, Data Analytics, and Software Development.

---
