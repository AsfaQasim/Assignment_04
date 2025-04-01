print("03 Fahrenheit Scale")

def temp():
    print("This code converts Fahrenheit to Celsius")
    fahrenheit_degree = float(input("Enter your Fahrenheit degree: "))
    celsius_degree = (fahrenheit_degree - 32) * 5.0 / 9.0
    print(f"Temperature in Celsius: {celsius_degree:.2f}°C")

if __name__ == "__main__":
    temp()