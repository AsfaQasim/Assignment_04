Days_per_year = 365
Hours_per_day = 24
Min_per_hour = 60
Second_per_min = 60

def main():
    total_seconds = Days_per_year * Hours_per_day * Min_per_hour * Second_per_min
    print("There are " + str(total_seconds) + " seconds in a year.")

if __name__ == "__main__":
    main()
