# sprint4_dashboard.py

def predict_temperature(x):
    if x < 0 or x > 100:
        print("Warning: x outside expected range (0-100)")
    return 1 * x**2 - 4 * x + 5

def predict_humidity(x): 
    return 0.5 * x**2 - 2 * x + 10

def predict_pressure(x): 
    return 1.2 * x

if __name__ == "__main__":
    x = float(input("Enter time step (x): "))
    temp = predict_temperature(x)
    humidity = predict_humidity(x)
    pressure = predict_pressure(x)

    print(f"Temperature: {temp:.2f} °C")
    print(f"Humidity: {humidity:.2f} %")
    print(f"Pressure: {pressure:.2f} hPa")
