def main():

grocerylist = {}                                        # Define the grocery list as a dict

    while True:                                         # Initiate an infinite loop to keep prompting the user
        try:
            item = input().upper()                      # Ask for an item

            if item not in grocerylist:                 # If the item isn't on the list already,
                grocerylist[item] = 1                   # put it there and set its value (amount) to 1
            else:
                grocerylist[item] += 1                  # Otherwise it's already there, so increase its value by 1.

        except EOFError:                                # When the user ends input

            for n in sorted(grocerylist.keys()):        # Sort the grocery list items (keys) alphabetically, and iterate through the items
                print(grocerylist[n], n)                # Print the value (amount) and then the name of the item (key)
                
            break                                       # Then stop

main()