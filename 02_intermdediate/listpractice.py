my_list = ["apple", "mango", "banana", "pineapple", "peach"]

def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return f"Element at index {index} is {my_list[index]}"
    return "Index out of range"

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        old_value = my_list[index]
        my_list[index] = new_value
        return f"Element at index {index} modified from {old_value} to {new_value}"
    return "Index out of range"

def slice_list(my_list, start, end):
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list) and start < end:
        return my_list[start:end]
    return "Invalid slice range"

def list_game():
    print("\nWelcome to the list manipulation game!")

    while True:
        print("\nCurrent list:", my_list)
        print("Select an operation:")
        print("1: Access Element")
        print("2: Modify Element")
        print("3: Slice List")
        print("4: Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            index = int(input("Enter the index of the element you want to access: "))
            print(access_element(my_list, index))

        elif choice == "2":
            index = int(input("Enter the index of the element you want to modify: "))
            new_value = input("Enter the new value for the element: ")
            print(modify_element(my_list, index, new_value))

        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print("Sliced list:", slice_list(my_list, start, end))

        elif choice == "4":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice! Please try again.")


list_game()
