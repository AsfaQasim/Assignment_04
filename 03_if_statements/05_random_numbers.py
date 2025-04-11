import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    print(f"Generating {N_NUMBERS} random numbers between {MIN_VALUE} and {MAX_VALUE}:")
    for i in range(N_NUMBERS):
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        print(f"Number {i + 1}: {random_number}")
if __name__ == "__main__":
    main()
