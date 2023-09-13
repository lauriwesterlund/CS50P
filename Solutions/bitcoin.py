import requests
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        Amount = float(sys.argv[1])

    except (ValueError):
        sys.exit("Command-line argument is not a number")

    Cost = Amount * get_bitcoin_price()
    print(f"${Cost:,.4f}")

def get_bitcoin_price():

    try:
        Data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        Data = Data.json()
        return Data["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        sys.exit("There was a problem retrieving the data.")


if __name__ == "__main__":
    main()