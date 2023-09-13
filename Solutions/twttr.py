def main():

    # Prompt user for input and prepare to print output
    tweet = input("Input: ")
    print("Output: " + shorten(tweet))

def shorten(word):
    # Iterate through each letter in the input
    # If it's not a vowel, store it in the output variable
    # Vowels get skipped.
    output = ""
        
    for letter in word:
        if letter.lower() not in 'aeiou':
            output = output + letter
    
    return output


if __name__ == "__main__":
    main()