def leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year! 🎉")
    else:
        print(f"{year} is NOT a Leap Year.")

if __name__ == "__main__":
    leap_year()