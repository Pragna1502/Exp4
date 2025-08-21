# sprint2_temp_humidity_pressure.py

def predict_temperature(x): 
    return 1 * x**2 - 4 * x + 5

def predict_humidity(x): 
    return 0.5 * x**2 - 2 * x + 10

def predict_pressure(x): 
    return 1.2 * x

if __name__ == "__main__":
    x = float(input("Enter time step (x): "))
    print(f"Temperature: {predict_temperature(x):.2f} °C")
    print(f"Humidity: {predict_humidity(x):.2f} %")
    print(f"Pressure: {predict_pressure(x):.2f} hPa")
