
def calculate_total_cost():
    fruit_price = {
        "apple": 5.9,
        "mango": 12.7,
        "pine apple": 23,
        "kiwi": 6.7,
        "orange": 4.7,
        "banana": 3.9
    }

    total_cost = 0

    for fruit, price in fruit_price.items():
        while True:
            try:
                quantity = int(input(f"How many {fruit} do you want? "))
                if quantity < 0:
                    print("Invalid input, please enter a non-negative number.")
                    continue
                total_cost += price * quantity
                break
            except ValueError:
                print("Invalid input, please enter a valid number.")

    print(f"\nYour total cost is {total_cost:.2f}.")


calculate_total_cost()
