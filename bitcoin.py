import requests
import json
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif not isFloat(sys.argv[1]):
        sys.exit("Command-line argument is not a number")
    else:
        try:
            request = requests.get(
                "https://rest.coincap.io/v3/assets?apiKey=6d42c8d91904a5b14c2b8182881b6f8023da39d15bfc41988fdf69c9e6527c97")
            data_obj = (request.json())["data"][0]
            print(json.dumps(data_obj, indent=2))
            # bitcoin_price = float(sys.argv[1])

            # for bitcoin_obj in data_obj:
            #     for key in bitcoin_obj:
            #         if bitcoin_obj[key] == "Bitcoin":
            #             amount = float(bitcoin_obj["priceUsd"]) * bitcoin_price
            #             print(f'{amount:,.4f}')
        except requests.RequestException:
            sys.exit("API Error")

def isFloat(args):
    try:
        float(args)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()

"""
Expects the user to specify as a command-line argument the number of Bitcoins,
, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinCap Bitcoin Price Index at https://api.coincap.io/v2/assets/bitcoin, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

import requests

try:
    ...
except requests.RequestException:
    ...

Outputs the current cost of
Bitcoins in USD to four decimal places, using , as a thousands separator.
"""
