from tabulate import tabulate
import sys
import csv

def main():

    # Check for correct command-line arguments (should be the name of a single CSV file or its path)
    check_arguments(sys.argv)

    # We're expecting a list of dictionaries containing the names of pizzas and their prices
    pizzas = pizzaReader(sys.argv[1])

    # Print as a pretty table
    print(tabulate(pizzas, headers="keys", tablefmt="grid"))


def pizzaReader(file):

    """ Reads a CSV file, expecting a list of pizzas and their prices, and returns it as a list of dictionaries"""
    pizzas = []

    try:
        with open(file) as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                pizzas.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")

    return pizzas
    
def check_arguments(args):

    """ Probes sys.argv for one single argument that should be a .csv file. """

    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    elif args[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()