print("01 dicesimulator")
import random

def roll_dice():
    dial1 = random.randint(1, 6)
    dial2 = random.randint(1, 6)
    total = dial1 + dial2
    print(f"Total of two dice: {total}")

def main():
    dial1 = 10
    print(f"dial1 in main() starts as: {dial1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"dial1 in main() is: {dial1}")

if __name__ == "__main__":
    main()
