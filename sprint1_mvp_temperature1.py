# sprint1_mvp_temperature.py

def predict_temperature(x):
    return 1 * x**2 - 4 * x + 5

if __name__ == "__main__":
    x = float(input("Enter time step (x): "))
    temp = predict_temperature(x)
    print(f"Predicted Temperature at x={x:.1f} is {temp:.2f}°C")
