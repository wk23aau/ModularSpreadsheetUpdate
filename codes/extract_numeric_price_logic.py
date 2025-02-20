import re # Import re here as it's used in this module

def extract_numeric_price(market_price):
    price_match = re.findall(r'\d+\.\d+|\d+', str(market_price))
    return float(price_match[0]) if price_match else None