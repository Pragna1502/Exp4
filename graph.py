import matplotlib.pyplot as plt

# Prediction models (simple quadratic & linear equations for demo)
def predict_temperature(x):
    return 1 * x**2 - 4 * x + 5   # Example: quadratic relation

def predict_humidity(x):
    return 0.5 * x**2 - 2 * x + 10   # Example: quadratic relation

def predict_pressure(x):
    return 1.2 * x + 1000   # Example: linear relation (base 1000 hPa)

# Generate predictions for 0 to 10 time steps
x_values = list(range(11))  # 0,1,2,...,10
temps = [predict_temperature(x) for x in x_values]
hums = [predict_humidity(x) for x in x_values]
press = [predict_pressure(x) for x in x_values]

# --- Plotting ---
plt.figure(figsize=(8,5))
plt.plot(x_values, temps, label='Temperature (°C)', color='red', marker='o')
plt.plot(x_values, hums, label='Humidity (%)', color='blue', marker='s')
plt.plot(x_values, press, label='Pressure (hPa)', color='green', marker='^')

plt.title("Weather Predictions Dashboard")
plt.xlabel("Time Step (x)")
plt.ylabel("Values")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()

# --- Optional: Save the graph as image ---
plt.savefig("weather_dashboard.png")
