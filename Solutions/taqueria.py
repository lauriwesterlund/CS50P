def main():

    total = 0                                       # The total price starts from 0.

    while True:                                     # Initiate an infinite loop to keep prompting.

        try:
            item = input("Item: ").title()          # Prompt for an item and titlecase the input.

            if item not in menu:                    # If the input doesn't exist on the menu, do nothing.
                pass
            else:                                   # Otherwise look up the item's price, add it to the total, then print the total.
                total = total + menu[item]
                print(f"Total: ${total:.2f}")

        except EOFError:                            # When the user ends input, print a new line and exit loop.
            print("")
            break


menu = {                                            # Menu items are defined here as a dictionary.
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


main()

