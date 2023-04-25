def main():

    # Prompt user for time
    clock = input("What time is it? ")

    # Convert time to decimals
    clock = convert(clock)

    # Check the results and let the user know if it's time to eat
    if 7.00 <= clock <= 8.00:
        print("breakfast time")

    elif 12.00 <= clock <= 13.00:
        print("lunch time")

    elif 18.00 <= clock <= 19.00:
        print("dinner time")

def convert(time):

    # Split the input in two
    x, y = time.split(":")

    x = float(x) # Hours
    y = float(y) # Minutes

    # Turn the minutes into decimals and add to hours, return the value
    return (x + (y * (1 / 60)))


if __name__ == "__main__":
    main()
