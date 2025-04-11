
sentence_start = "Panaversity is fun. I learned to program and used Python to make my"

def mad_libs():
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    print(f"{sentence_start} {adjective} {noun} {verb}!")

if __name__ == "__main__":
    mad_libs()
