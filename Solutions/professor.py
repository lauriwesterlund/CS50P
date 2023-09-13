import random


def main():

    # Call get_level function to prompt the user for a level between 1-3
    Level = get_level()

    # Define some variables to keep track of the number of problems and attempts, and the total score
    Problems = 0
    Attempt = 0
    Score = 0

    # Loop through ten problems
    while Problems < 10:

        # Generate two integers and store their sum
        Int1 = generate_integer(Level)
        Int2 = generate_integer(Level)
        Result = Int1 + Int2

        # Prompt the user continuously for an answer
        while True:
            try:
                Answer = int(input(f"{Int1} + {Int2} = "))

                # Wrong answer get EEE, increase the Attempt variable to keep track of attempts
                if Answer != Result:
                    print("EEE")
                    Attempt += 1

                    # If this was the final attempt, print the correct result and move on to the next problem.
                    if Attempt == 3:
                        print(f"{Int1} + {Int2} = {Result}")
                        Attempt = 0
                        Problems += 1
                        break

                # If the answer was correct, increase score and move on to the next problem.
                elif Answer == Result:
                    Attempt = 0
                    Score += 1
                    Problems += 1
                    break

            # Catch bad inputs here
            except(TypeError, ValueError):
                pass

    # Once all problems have been attempted/solved, print the final score.
    print(f"Score: {Score}")


def get_level():

    # Infinite loop to prompt user for a positive integer between 1 and 3.
    while True:
        try:
            Level = int(input("Level: "))

        # Bad inputs get caught here
        except(ValueError, TypeError):
            pass

        # If the input is one of the desired values, return the value and exit loop
        if Level == 1 or Level == 2 or Level == 3:
            return Level


def generate_integer(level):

    # Define range depending on number of integers required
    startRange = 10**(level - 1)
    endRange = 10**(level) - 1

    # Return the generated number
    return random.randint(startRange, endRange)


if __name__ == "__main__":
    main()