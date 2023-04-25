def main():

    # Prompt user for input
    camelcase = input("camelCase: ")

    # Print this first without starting a new line
    print("snake_case: ", end="")

    # Iterate through letters in the user's input.
    # If the letter is lowercase, print it as-is
    # If the letter is uppercase, add a "_" and then print the letter in lowercase
    # Always override the default new line at the end of print with end=""

    for letter in camelcase:
        if letter.islower():
            print(letter, end="")
        else:
            print("_" + letter.lower(), end="")

    # Finally, print a new empty line at the end
    print("")


main()