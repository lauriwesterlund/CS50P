def main():
    text = input()
    print(convert(text))

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()