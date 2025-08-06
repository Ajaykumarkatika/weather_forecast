import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual OpenWeatherMap API key
API_KEY = 'cc5f211d2a9506a056b98b6ec96e81ca'
CITY = 'Delhi'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Check for errors in response
if response.status_code != 200 or 'list' not in data:
    print("❌ Error fetching data from API:")
    print(data)
    exit()

# Extract temperature and time
temps = []
times = []

for entry in data['list'][:8]:  # Next 24 hours (3-hour intervals)
    temps.append(entry['main']['temp'])
    times.append(entry['dt_txt'])

# Plotting
plt.figure(figsize=(10, 5))
sns.lineplot(x=times, y=temps, marker='o')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_plot.png")
plt.show()
