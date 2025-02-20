PRODUCT_CATEGORIES = [ # Define PRODUCT_CATEGORIES here as it's used in this module
    "Electronics", "Books", "Clothing", "Home & Garden", "Beauty", "Toys & Games"
]

def get_product_category(category_names, category_urls, heading, summary_text):
    text_to_analyze = " ".join(category_names + category_urls + [heading, summary_text]).lower()
    for category in PRODUCT_CATEGORIES:
        if category.lower() in text_to_analyze:
            return category
    return "default"