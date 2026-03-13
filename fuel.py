def main():
    percentage = get_percentage()

    #Check for empty, full or standard %
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")

def get_percentage():
    while True:
        fraction = input("Fraction: ")
        try:
            #split fraction into x and y
            x_str, y_str = fraction.split("/")
            #convert to integers
            x = int(x_str)
            y = int(y_str)
            # check if x > y or y = 0
            #Ensure x and y are positive AND x is not greater than y
            if x < 0 or y <= 0 or x > y:
                continue
            #do calc and round to nearest int
            #This raises ZeroDivisionError if y = 0
            return round( (x / y) * 100)
        except (ValueError, ZeroDivisionError):
            #If any errors, loop restarts
            pass

if __name__ == "__main__":
    main()
