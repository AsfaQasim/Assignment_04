import math

print("04 pythagorean_theorem")

def main():
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    bc = math.sqrt(ab**2 + ac**2)

    print(f"The length of BC (hypotenuse) is {bc:.2f}")

if __name__ == "__main__":
    main()
