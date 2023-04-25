def main():
    x = int(input("What's x? "))

    if even(x):
        print("Even")
    else:
        print("Odd")

def even(n):
    return n % 2 == 0

main()