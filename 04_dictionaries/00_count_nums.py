def count():
    count_dict = {}

    while True:
        user_input = input("Enter a number (or type 'Exit' to quit): ")

        if user_input.title() == "Exit":
            break
        elif user_input.isdigit():
            num = int(user_input)
            count_dict[num] = count_dict.get(num, 0) + 1
        else:
            print("Invalid input. Please input a number or 'Exit'.")

    print("\nCount Summary:")
    for key, value in count_dict.items():
        print(f"{key}: {value}")


count()
