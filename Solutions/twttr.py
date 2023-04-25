def main():

    tweet = input("Input: ")                # Prompt user for input
    print("Output: ", end="")               # Start printing output, skip the new line

    for letter in tweet:                    # Iterate through each letter in the input
        if letter.lower() not in 'aeiou':   # If it's not a vowel,
            print(letter, end="")           # print it.
            
    print("")                               # Print a new line at the end

main()
