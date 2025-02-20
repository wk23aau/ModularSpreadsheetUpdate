import re # Import re here as it's used in this module

def extract_product_id(url):
    match = re.search(r'/ip/(\d+)', url)
    return str(match.group(1)) if url and match else ""