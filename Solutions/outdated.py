def main():

    # Initiate an infinite loop for continuous prompting
    while True:

        # Ask the user for input and try to pass it through the conversion function
        try:
            user_input = input("Date: ").strip()
            user_input = ISO8601_convert(user_input)
            print(user_input)
            break

        # This catches bad inputs, e.g. wrong format or numbers that don't make a valid date
        except (ValueError):
            pass

        # Cleaner exit if the user does Ctrl + D or Ctrl + C
        except (EOFError, KeyboardInterrupt):
            print("")
            break


def ISO8601_convert(date):

    # First check for mm/dd/yyy format by splitting along the slashes
    try:
        m, d, y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)

        # Throw an exception if the numbers are silly
        if m <= 0 or m > 12 or d <= 0 or d > 31 or y <= 0:
            raise ValueError
        # Otherwise, return the whole thing as a string, including leading zeroes where necessary
        else:
            return (f"{str(y).zfill(4)}-{str(m).zfill(2)}-{str(d).zfill(2)}")

    # If the split doesn't work as expected, try the other format instead
    except ValueError:

        try:
            # Try to split the date in three pieces along whitespaces
            m, d, y = date.split()
            # Turn the month into a number by looking it up from the list
            m = int(months.index(m) + 1)
            y = int(y)

            # Make sure there's a comma after the day, and if not, raise ValueError to prompt again
            if d[-1] == ",":
                d = int(d.replace(",", ""))
            else:
                raise ValueError

            # Check again for silly numbers
            if m <= 0 or m > 12 or d <= 0 or d > 31 or y <= 0:
                raise ValueError
            # Return properly formatted date if everything checks out
            else:
                return (f"{str(y).zfill(4)}-{str(m).zfill(2)}-{str(d).zfill(2)}")

        # If we still get a ValueError here, then the input was definitely bad and we need to prompt again
        except ValueError:
            raise ValueError




months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


main()
