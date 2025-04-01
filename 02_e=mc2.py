print("02 e=mc².md")

def energy():
    c = 299792458
    m = float(input("Enter mass in kilograms: "))

    energy_in_joules = m * (c ** 2)
    print("\ne = m * c²...")
    print(f"Mass = {m} kg")
    print(f"C = {c} m/s")
    print(f"Energy = {energy_in_joules} joules!")

energy()