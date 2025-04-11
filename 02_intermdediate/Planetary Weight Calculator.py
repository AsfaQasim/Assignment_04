def main():
    print("Welcome to the Planetary Weight Calculator")
    print("******************************************")
earth_weight = float(input("Enter your weight on earth: "))

gravity_ratio = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus" : 0.92,
    "Neptune": 1.19
}
print("\n Select a planet")

for planet in gravity_ratio:
    print(f"{planet}")
planet_choice = input("Enter the name of the planet: ").title()

if planet_choice in gravity_ratio:
    new_weight = earth_weight * gravity_ratio [planet_choice]
    print(f"Your weight on {planet_choice} is {new_weight:.2f} kg")
else:
    print("Invalid planet name")
if __name__ == "__main__":
    main()