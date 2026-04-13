import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# CONFIG SETTINGS
# ------------------------------
API_KEY = "4eb31466422863945268e792ee9e4b17"  # 🔺 Replace with your OpenWeatherMap API key
CITY = "Pune"             # You can change the city
UNITS = "metric"          # metric = Celsius

# ------------------------------
# FETCH WEATHER DATA FROM API
# ------------------------------
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"
response = requests.get(url)

if response.status_code != 200:
    print("Error fetching data:", response.json())
    exit()

data = response.json()

# ------------------------------
# EXTRACT USEFUL FIELDS
# ------------------------------
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
wind_speed = data["wind"]["speed"]

labels = ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)", "Wind Speed (m/s)"]
values = [temperature, humidity, pressure, wind_speed]

# ------------------------------
# SEPARATE VISUALIZATIONS
# ------------------------------
import matplotlib.pyplot as plt

# -------- GRAPH 1 (Temp, Humidity, Wind Speed) --------
plt.figure(figsize=(10, 6))
labels_main = ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"]
values_main = [temperature, humidity, wind_speed]

plt.bar(labels_main, values_main, color=["skyblue", "lightgreen", "violet"])
plt.title(f"Weather Dashboard for {CITY} (Main Parameters)")
plt.xlabel("Weather Parameters")
plt.ylabel("Values")
plt.tight_layout()
plt.savefig("output/main_parameters.png")
plt.show()


# -------- GRAPH 2 (PRESSURE ONLY) --------
print("Pressure =", pressure)   # debug print

plt.figure(figsize=(6, 5))
plt.bar(["Pressure (hPa)"], [pressure], color="orange")
plt.title(f"Atmospheric Pressure for {CITY}")
plt.ylabel("Pressure (hPa)")
plt.tight_layout()
plt.savefig("output/pressure.png")
plt.show()