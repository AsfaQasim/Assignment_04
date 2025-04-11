def add_number(numbers) -> int:
    num = 0
    for i in numbers:
        num += i
    return num
def main():
    numbers: list[int] = [1, 2, 3, 4, 5]
    total_sum = add_number(numbers)
    print(total_sum)

if __name__ == "__main__":
    main()
