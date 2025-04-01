print("05 Triangle Parameter..")

def triangle():
    print("This code is about the sum of triangle sides.")

    side1: float = float(input("Enter your first side no of the triangle: "))
    side2: float = float(input("Enter your second side no of the triangle: "))
    side3: float = float(input("Enter your third side no of the triangle: "))

    total: float = side1 + side2 + side3

    print(f"The parameter of triangle is {side1}, {side2}, and {side3} is {total}.")

if __name__ == "__main__":
    triangle()