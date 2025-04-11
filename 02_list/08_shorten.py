
Max_length = 4

def shorter(lst):
    while len(lst) > Max_length:
        lst.pop()
    if lst:
        last_element = lst.pop()
        print("Last removed element:", last_element)

def get_list():
    lst = []
    element = input("Enter an element to add to the list (press Enter to stop): ")
    while element != "":
        lst.append(element)
        element = input("Enter an element to add to the list (press Enter to stop): ")
    return lst

def main():
    lst = get_list()
    print("Original list:", lst)
    shorter(lst)
    print("Shortened list:", lst)

if __name__ == "__main__":
    main()
