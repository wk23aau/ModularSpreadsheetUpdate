import json
import logging

# --- Part 0: Configure logging (for standalone test) ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_categories(breadcrumbs_json):
    category_names = [""] * 4
    category_urls = [""] * 4
    try:
        breadcrumbs = json.loads(breadcrumbs_json)
        if isinstance(breadcrumbs, list):
            for idx, breadcrumb in enumerate(breadcrumbs[:4]):
                if isinstance(breadcrumb, dict):
                    category_names[idx] = breadcrumb.get("name", "")
                    category_urls[idx] = breadcrumb.get("url", "")
    except json.JSONDecodeError:
        logging.warning(f"Could not parse breadcrumbs JSON: {breadcrumbs_json}")
    return category_names, category_urls

# Example breadcrumbs JSON data from your message
example_breadcrumbs_json = """
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":{"@type":"Thing","@id":"https://www.walmart.com/cp/household-essentials/1115193","name":"Household Essentials"}},{"@type":"ListItem","position":2,"item":{"@type":"Thing","@id":"https://www.walmart.com/browse/household-essentials/household-essentials-by-brand/1115193_8250903","name":"Household Essentials by Brand"}},{"@type":"ListItem","position":3,"item":{"@type":"Thing","@id":"https://www.walmart.com/browse/household-essentials/dawn-dish-soap/1115193_8250903_8960327_2262803","name":"Dawn"}},{"@type":"ListItem","position":4,"item":{"@type":"Thing","@id":"https://www.walmart.com/browse/household-essentials/dawn-dish-soap/1115193_8250903_8960327_2262803","name":"Dawn Dish Soap"}}]}
"""

# Test the function
category_names, category_urls = extract_categories(example_breadcrumbs_json)

# Print the results
print("Extracted Category Names:", category_names)
print("Extracted Category URLs:", category_urls)