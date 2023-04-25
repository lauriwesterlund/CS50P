def main():

    fuel = get_fraction("Fraction: ")               # Prompt user for a fraction by calling get_fraction.

    if fuel <= 1:                                   # If prompt was successful, print results accordingly.
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

def get_fraction(prompt):

    while True:                                     # Initiate an infinite loop to keep prompting.

        try:
            x, y = input(prompt).split("/")         # Ask the user for input and split it into x and y.
            x = int(x)                              # Turn the values into integers.
            y = int(y)
            fraction = x/y                          # Perform division.

            if x > y or x < 0 or y < 0:             # Reprompt if either number was negative, or x > y.
                pass
            else:                                   # Otherwise round to the nearest integer and return the value.
                return round(fraction * 100)

        except (ValueError, ZeroDivisionError):     # Catch any errors. Non-integers or multiple slashes result in ValueError, y == 0 causes ZeroDivisionError.
            pass

main()