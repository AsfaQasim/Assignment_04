def get_last_element(lst):
    if lst:
        print("Last element:", lst[-1])
    else:
        print("The list is empty.")

def get_list():
    lst = []
    elem = input("Enter an element to add to the list (press Enter to stop): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter an element to add to the list (press Enter to stop): ")
    return lst

def main():
    lst = get_list()
    get_last_element(lst)

if __name__ == "__main__":
    main()