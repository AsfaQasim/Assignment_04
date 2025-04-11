print("05 remainder_division")

def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")

if __name__ == "__main__":
    main()