def main():

    list = []                               # Make an empty list for the user's inputs
    total = {}                              # Make an empty dict for storing the total amounts

    while True:
        try:
            item = input("").upper()        # Prompt the user for input
            list.append(item)               # Add it to the end of the list
            list.sort()                     # Sort the list alphabetically

        except EOFError:                    # When user ends input

            for item in list:               # Iterate through the list
                if item not in total:       # If the item is not yet in the dict
                    total[item] = 1         # Put it there and give it a value of 1
                else:
                    total[item] += 1        # Otherwise increase its value by 1

            for _ in total:                 # Iterate through each item in the dict
                print(f"{total[_]} {_}")    # Print the value (amount), a space, and the item's name

            break                           # Then stop

main()