def main():

    # Ask the user for input, assume correct formatting
    # Strip and split it, then store into three variables

    x, y, z = input("Expression: ").strip().split()
    x = float(x)
    z = float(z)

    # Perform the arithmetic depending on the operator, store the answer
    
    match y:
        case "+":
            answer = x + z
        case "-":
            answer = x - z
        case "*":
            answer = x * z
        case "/":
            answer = x / z

    # Print the answer
    print(f"{answer:.1f}")

main()