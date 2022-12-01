import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        number_of_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number.")
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        out = response.json()
        rate_float = out["bpi"]["USD"]["rate_float"]
        # print(rate_float)
        total_cost = rate_float * number_of_bitcoins
        print(f"${total_cost:,.4f}")
    except requests.RequestException:
        sys.exit("404")


if __name__ == "__main__":
    main()
