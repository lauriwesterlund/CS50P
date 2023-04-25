def main():

    # Prompt user for input and prepare to print output
    tweet = input("Input: ")
    print("Output: ", end="")

    # Iterate through each letter in the input
    # If it's not a vowel, print it.
    # Vowels get skipped.
    for letter in tweet:
        if letter.lower() not in 'aeiou':
            print(letter, end="")

    # Print a new line at the end
    print("")

main()