def main():
    name = input("What's your name? ").strip().title()
    first, last = name.split(" ")

    hello()
    hello(first)

def hello(to="world"):
    print("Hello,", to)

main()