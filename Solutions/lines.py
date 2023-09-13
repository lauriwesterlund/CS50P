import sys

def main():

    check_arguments(sys.argv)
    print(check_lines(sys.argv[1]))

def check_arguments(args):

    """ Probes sys.argv for one single argument that should be a python file. """

    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    elif args[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    
def check_lines(file):
    
    """ Checks the number of lines in a python file, not including comments, docstrings, or blank lines. """
    linecount = 0

    try:
        with open(file) as file:

            # Iterate through lines in the file
            for line in file:

                # If the line is a comment or a docstring, do nothing
                if line.lstrip().startswith("***") or line.lstrip().startswith("#"):
                    pass
                # If the line is empty or has only spaces in it, do nothing
                elif line == "\n" or line.lstrip() == "": 
                    pass
                # Otherwise count the line
                else:
                    linecount += 1

    # In case the file doesn't exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    return linecount

if __name__ == "__main__":
    main()