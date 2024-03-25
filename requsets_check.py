import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    float(sys.argv[-1])
except ValueError:
    sys.exit("Invalid command-line argument")

r = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice.json", auth=("user", "pass")
)

info = r.json()
price = info["bpi"]["USD"]["rate"]
amount = float(price.replace(",", "")) * float(sys.argv[-1])
print(f"${amount:,.4f}")
