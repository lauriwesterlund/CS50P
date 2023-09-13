import sys
import csv

def main():

    # Check for correct command-line arguments (two CSV files, one for reading and one for writing)
    check_arguments(sys.argv)

    # Create a cleaned up version of the original file
    scourgify(sys.argv[1], sys.argv[2])


def scourgify(input, output):

    """ Read a CSV file and make a new one where the students' first and last names are split to their own columns"""
    newFile = []


    # Read through the source file
    try:
        with open(input) as file:
            reader = csv.DictReader(file)

            # Split the first and last names, and hold everything in newFile
            for row in reader:
                last, first = row["name"].split(", ")
                newFile.append({"first": first, "last": last, "house": row["house"]})

    # Except if the source file doesn't exist
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")

    # Write a new file with the information stored in newFile
    with open(output, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in newFile:
            writer.writerow(row)

def check_arguments(args):

    """ Probes sys.argv for two arguments: a CSV file to read and a CSV file to write to"""

    if len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    elif args[1].endswith(".csv") == False:
        sys.exit(f"Could not read {args[1]}")
    elif args[2].endswith(".csv") == False:
        sys.exit(f"Could not write to {args[2]}")

if __name__ == "__main__":
    main()
