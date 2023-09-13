import sys
import os
from PIL import Image, ImageOps

def main():

    # Check for correct command-line arguments (two CSV files, one for reading and one for writing)
    check_arguments(sys.argv)

    # Create a cleaned up version of the original file
    paste_shirt(sys.argv[1], sys.argv[2])


def paste_shirt(input, output):

    """ Pastes a CS50 shirt on an image """

    image1 = Image.open(input)
    image2 = Image.open("shirt.png")

    newImage = ImageOps.fit(image1, image2.size)

    newImage.paste(image2, image2)
    newImage.save(output)

def check_arguments(args):

    """ Probes sys.argv for two JPG/PNG images"""

    # Make sure we have the correct amount of command-line arguments
    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")

    # Defining supported filetypes
    supported = [".jpg", ".jpeg", ".png"]

    # Find out the extensions of both files
    input = os.path.splitext(args[1])
    output = os.path.splitext(args[2])

    # If we have unsupported extensions, exit the program
    if input[1] not in supported:
        sys.exit(f"Could not read {args[1]}")

    elif output[1] not in supported:
        sys.exit(f"Could not read {args[2]}")

    elif input[1] != output[1]:
       sys.exit(f"{args[1]} and {args[2]} are different file types.")


if __name__ == "__main__":
    main()