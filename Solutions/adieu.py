import inflect
    
def main():

    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)

        except(EOFError, KeyboardInterrupt):

            names = p.join(names)
            print("Adieu, adieu, to " + names)
            quit()

main()