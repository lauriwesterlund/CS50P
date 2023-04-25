def main():
    # Price of coke is 50 cents.
    price = 50

    # While the price is greater than zero, i.e. not paid in full
    while price > 0:

        # Print the amount due
        print(f"Amount Due: {price}")

        # Prompt the user for a coin
        coins = int(input("Insert Coin: "))

        # Only accept 10, 25 or 50 cent coins. Otherwise keep looping.
        if coins == 10 or 25 or 50:
            price = price - coins

    # Once the coke is paid, return the difference as an absolute value.
    print(f"Change owed: {abs(price)}")

main()