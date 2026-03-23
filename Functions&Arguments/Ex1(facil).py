def main():
    celsius = float(input("Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print(f"{result:.2f}°F")

def celsius_to_fahrenheit(c: float):
    return (c * 9/5) + 32

main()