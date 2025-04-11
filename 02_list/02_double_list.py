def main():
    numbers: list[int] = [1, 2, 3, 4, 5]


    for i in range(len(numbers)):
        numbers[i] *= 2

    print(numbers)

if __name__ == "__main__":
    main()