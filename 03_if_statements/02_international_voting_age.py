
PETURKSBOUIPO_AGE: int = 16
STANLAU_AGE: int = 25
MAYENGUA_AGE: int = 48

def main():

    age = int(input("How old are you? "))


    if age >= PETURKSBOUIPO_AGE:
        print(f"Your age is {age}. You are eligible to vote in PETURKSBOUIPO.")
    else:
        print(f"Your age is {age}. You are not eligible to vote in PETURKSBOUIPO.")

    if age >= STANLAU_AGE:
        print(f"Your age is {age}. You are eligible to vote in STANLAU.")
    else:
        print(f"Your age is {age}. You are not eligible to vote in STANLAU.")

    if age >= MAYENGUA_AGE:
        print(f"Your age is {age}. You are eligible to vote in MAYENGUA.")
    else:
        print(f"Your age is {age}. You are not eligible to vote in MAYENGUA.")

if __name__ == "__main__":
    main()
