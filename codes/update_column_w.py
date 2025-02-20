import logging

PRODUCT_CATEGORIES_MAPPING = {
    "Apparel & Accessories": ["apparel", "accessories", "clothing", "handbags", "sunglasses", "shoes"],
    "Automotive & Powersports": ["automotive", "powersports", "tires", "wheels"],
    "Automotive Electronics": ["automotive electronics"],
    "Baby": ["baby"],
    "Beauty": ["beauty", "makeup", "skincare", "fragrance"],
    "Books": ["books"],
    "Camera & Photo": ["camera", "photo", "binoculars", "telescopes", "spotting scopes", "night vision goggles", "hunting trail monitors"],
    "Cell Phones": ["cell phones", "mobile phones"],
    "Consumer Electronics": ["consumer electronics"],
    "Compact Appliances": ["compact appliances"],
    "Electronics Accessories": ["electronics accessories"],
    "Decor": ["decor", "decoration"],
    "Gourmet Food": ["gourmet food"],
    "Grocery": ["grocery", "food", "beverages"],
    "Health & Personal Care": ["health", "personal care", "health & personal care"],
    "Home & Garden": ["home", "garden", "home & garden", "furniture", "indoor furniture", "outdoor furniture", "outdoor power tools", "plumbing", "heating", "cooling", "ventilation", "kitchen", "decor"], # Added decor here as it seems related to Home & Garden
    "Industrial & Scientific": ["industrial", "scientific", "industrial & scientific"],
    "Jewelry": ["jewelry", "watches"], # Added watches here as it seems related to Jewelry based on referral fee table
    "Kitchen": ["kitchen"],
    "Luggage & Travel Accessories": ["luggage", "travel accessories"],
    "Major Appliances": ["major appliances"],
    "Music": ["music"],
    "Musical Instruments": ["musical instruments"],
    "Office Products": ["office products", "calculators", "printer cartridges"],
    "Outdoor Power Tools": ["outdoor power tools"],
    "Outdoors": ["outdoors", "sporting goods", "outdoor recreation"], # General outdoors + sporting goods
    "Personal Computers": ["personal computers", "pc", "desktops", "laptops"],
    "Pet Supplies": ["pet supplies"],
    "Plumbing, Heating, Cooling & Ventilation": ["plumbing", "heating", "cooling", "ventilation"],
    "Shoes, Handbags & Sunglasses": ["shoes", "handbags", "sunglasses"],
    "Software & Computer Video Games": ["software", "computer games", "video games"],
    "Sporting Goods": ["sporting goods", "sports"],
    "Tires & Wheels": ["tires", "wheels"],
    "Tools & Home Improvement": ["tools", "home improvement", "base power tools"],
    "Toys & Games": ["toys", "games", "toys & games"],
    "Video & DVD": ["video", "dvd"],
    "Video Game Consoles": ["video game consoles"],
    "Watches": ["watches"],
    "Everything Else": [], # Default category, no specific keywords needed
    "default": [] # Fallback default
}


PRODUCT_CATEGORIES_LIST = list(PRODUCT_CATEGORIES_MAPPING.keys()) # Create a list of product categories


def get_product_category(category_names, category_urls, heading, summary_text):
    """
    Determines the product category based on category names, URLs, heading, and summary text,
    using a keyword-based mapping to product categories and referral fee criteria.

    Args:
        category_names: List of category names extracted from breadcrumbs.
        category_urls: List of category URLs extracted from breadcrumbs.
        heading: Product heading/title.
        summary_text: Product summary/description.

    Returns:
        The determined product category as a string (e.g., "Electronics", "Clothing", "default").
    """
    text_to_analyze = " ".join(category_names + category_urls + [heading, summary_text]).lower()

    for category, keywords in PRODUCT_CATEGORIES_MAPPING.items():
        for keyword in keywords:
            if keyword.lower() in text_to_analyze:
                return category # Return the category if keyword is found

    # If no category matched based on keywords, return "default"
    return "default"


def update_column_w_sheet(worksheet, product_category_col_index, start_row, num_rows, new_rows):
    """
    Updates Column W (Product Category) in the Google Sheet based on extracted category information
    using the get_product_category function.

    Args:
        worksheet: The Google Sheet worksheet object.
        product_category_col_index: The column index for 'Product Category' (e.g., "W").
        start_row: The starting row number for updates.
        num_rows: The number of rows to update.
        new_rows: A list of lists, where each inner list is a row of data,
                   and category names and URLs are expected to be in specific columns
                   (currently columns 14-21 based on main script's new_row_data structure).
    """
    logging.info("Updating Column W (Product Category) in Google Sheet...")
    cells_to_update = []
    for i in range(num_rows):
        row_index = start_row + i
        category_names = new_rows[i][14:18] # Categories are in columns O, P, Q, R (index 14-17 in new_row_data)
        category_urls = new_rows[i][18:22] # Category URLs are in columns S, T, U, V (index 18-21 in new_row_data)
        heading = new_rows[i][2] # Heading in column C (index 2)
        summary_text = new_rows[i][10] # Summary in column K (index 10)


        product_category = get_product_category(category_names, category_urls, heading, summary_text)


        cell_coordinate = f"{product_category_col_index}{row_index}"
        cells_to_update.append({'range': cell_coordinate, 'values': [[product_category]]})

    if cells_to_update:
        worksheet.batch_update(cells_to_update)
        logging.info(f"Column W (Product Category) updated for rows {start_row} to {start_row + num_rows - 1}.")
    else:
        logging.info("No updates needed for Column W (Product Category).")