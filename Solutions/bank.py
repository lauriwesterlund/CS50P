def main():
    answer = input("Greeting: ").strip().lower()

    print(f"${value(answer)}")

def value(x):

    if x.startswith("hello"):
        return(0)
    elif x.startswith("h"):
        return(20)
    else:
        return(100)


main()
