def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")

# Requirements to pass:
# - Two to six letters or numbers (no punctuation, spaces, etc)
# - Must start with at least two letters
# - Numbers can't be in the middle of the plate
# - The first number can't be a zero

def is_valid(s):

    length = len(s)                                                         # Get the length of the plate

    if 2 <= length <= 6 and s[0:length].isalnum() and s[0:2].isalpha():     # Only proceed if length is 2-6, all chars are alphanumeric, and the first two characters are letters.

        for _ in range(length - 1):                                         # Iterate through the input one character at a time, and return false, if...

                if s[_].isdigit() and s[_ + 1].isalpha():                   # a number is followed by a letter (i.e. numbers in the middle)
                    return False

                if s[_] == "0" and s[_ - 1].isalpha():                      # a zero is preceded by a letter (i.e. it's the first number)
                    return False

        return True                                                         # If neither of the above have returned false, then return true.

main()
