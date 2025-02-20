import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import tkinter as tk
from tkinter import filedialog
import json
import logging

# --- Part 0: Configure logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Import column update functions from separate files
from update_headers import update_headers_sheet
from update_column_a import update_column_a_sheet
from update_column_b import update_column_b_sheet
from update_column_c import update_column_c_sheet
from update_column_d import update_column_d_sheet
from update_column_e import update_column_e_sheet
from update_columns_f_to_j import update_columns_f_to_j_sheet
from update_column_k import update_column_k_sheet
from update_column_l import update_column_l_sheet
from update_column_m import update_column_m_sheet
from update_column_n import update_column_n_sheet
from update_column_o import update_column_o_sheet
from update_column_p import update_column_p_sheet
from update_column_q import update_column_q_sheet
from update_column_r import update_column_r_sheet
from update_column_s import update_column_s_sheet
from update_column_t import update_column_t_sheet
from update_column_u import update_column_u_sheet
from update_column_v import update_column_v_sheet
from update_column_w import update_column_w_sheet
from update_column_x import update_column_x_sheet
from update_column_y import update_column_y_sheet
from update_column_z import update_column_z_sheet
from update_column_aa import update_column_aa_sheet
from update_column_ab import update_column_ab_sheet
from update_column_ac import update_column_ac_sheet
from update_column_ad import update_column_ad_sheet # Import update_column_ad_sheet
from update_column_ae import update_column_ae_sheet # Import update_column_ae_sheet (new)


# Import extraction logic from separate files
from extract_images_logic import extract_images
from extract_summary_logic import extract_summary
from extract_key_features_logic import extract_key_features
from extract_categories_logic import extract_categories # Ensure this import is present
from get_product_category_logic import get_product_category
from calculate_referral_fee_logic import calculate_referral_fee
from extract_details_keyword_grouped_logic import extract_details_keyword_grouped
from extract_details_excel_keyword_grouped_logic import extract_details_excel_keyword_grouped
from load_excel_logic import load_excel
from extract_product_id_logic import extract_product_id
from extract_numeric_price_logic import extract_numeric_price
from get_random_brand_logic import get_random_brand


# --- Part 1: Constants and Setup ---
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "15QxK3A3uYjZNveb7qWFIZsuKJ7K1W9OozFksXdlapIg"
SPREADSHEET_NAME = "Products Data V1"
CREDENTIALS_FILE = "./credentials.json"
IMAGE_COLUMN_COUNT = 5
DEFAULT_SELLING_PRICE = 9.99
LIGHT_ORANGE_HEX = "#FFE0B2"
LIGHT_GREEN_HEX = "#C8E6C9"
DEFAULT_REFERRAL_FEE = 9.99
DEFAULT_LABEL_FEE = 4.5
DEFAULT_PROCESSING_FEE = 0.5

CATEGORY_REFERRAL_FEES = {
    "Electronics": 0.05,
    "Books": 0.07,
    "Clothing": 0.10,
    "Home & Garden": 0.12,
    "Beauty": 0.08,
    "Toys & Games": 0.09,
    "default": 0.15,
}

PRODUCT_CATEGORIES = [
    "Electronics", "Books", "Clothing", "Home & Garden", "Beauty", "Toys & Games"
]


# --- Part 2: Corrected extract_categories function ---
def extract_categories(breadcrumbs_json):
    category_names = [""] * 4
    category_urls = [""] * 4
    try:
        breadcrumbs_dict = json.loads(breadcrumbs_json) # Parse JSON into a dictionary
        item_list_element = breadcrumbs_dict.get("itemListElement") # Get the itemListElement

        if isinstance(item_list_element, list): # Now check if itemListElement is a list
            for idx, breadcrumb in enumerate(item_list_element[:4]): # Iterate over itemListElement
                if isinstance(breadcrumb, dict):
                    item = breadcrumb.get("item", {}) # Get the 'item' dictionary
                    category_names[idx] = item.get("name", "") # Extract name from 'item'
                    category_urls[idx] = item.get("@id", "") # Extract URL (@id) from 'item'
    except json.JSONDecodeError:
        logging.warning(f"Could not parse breadcrumbs JSON: {breadcrumbs_json}")
    return category_names, category_urls


# --- Part 4: Google Sheets Interaction ---
def authenticate_gspread(creds_path=CREDENTIALS_FILE):
    logging.info("Authenticating with Google Sheets...")
    creds = Credentials.from_service_account_file(creds_path, scopes=SCOPES)
    client = gspread.authorize(creds)
    logging.info("Google Sheets authentication successful.")
    return client

def get_worksheet(client, sheet_id=SPREADSHEET_ID, sheet_index=0):
    logging.info(f"Opening worksheet with ID: {sheet_id}...")
    sheet = client.open_by_key(sheet_id)
    worksheet = sheet.get_worksheet(sheet_index)
    logging.info(f"Worksheet '{worksheet.title}' opened successfully.")
    return worksheet

def get_existing_product_ids(worksheet):
    logging.info("Fetching existing product IDs from sheet...")
    existing_data = worksheet.get_all_values()
    product_ids = {row[1].strip(): idx + 1 for idx, row in enumerate(existing_data) if len(row) > 1}
    logging.info(f"Found {len(product_ids)} existing product IDs.")
    return product_ids

def batch_update_sheet(worksheet, updates):
    if updates:
        logging.info(f"Batch updating sheet with {len(updates)} updates...")
        worksheet.batch_update(updates)
        logging.info("Batch update completed.")

def append_new_rows_sheet(worksheet, new_rows):
    if new_rows:
        logging.info(f"Appending {len(new_rows)} new rows to sheet...")
        next_row = len(worksheet.get_all_values()) + 1
        rows_to_insert = [row[:-1] for row in new_rows]
        worksheet.insert_rows(rows_to_insert, row=next_row)
        logging.info(f"Appended new rows starting from row {next_row}.")
        return next_row
    return None


# --- Part 5: Column Indexing ---
def get_column_indices():
    selling_price_column_index = "Z"
    referral_fee_column_index = "X"
    product_category_column_index = "W"
    shipping_column_index = "Y"
    label_fee_column_index = "AA"
    processing_fee_column_index = "AB"
    profit_loss_column_index = "AC"
    detail_columns_start_index = "AD"
    details_raw_column_index = "AE" # <-- Added details_raw_column_index


    sku_column_index = "A"
    product_id_col_index = "B"
    heading_col_index = "C"
    brand_col_index = "D"
    price_col_index = "E"
    image_1_column_index = "F"
    image_2_column_index = "G"
    image_3_column_index = "H"
    image_4_column_index = "I"
    image_5_column_index = "J"
    summary_column_index = "K"
    key_feature_1_column_index = "L"
    key_feature_2_column_index = "M"
    remaining_key_features_column_index = "N"
    category_1_column_index = "O"
    category_2_column_index = "P"
    category_3_column_index = "Q"
    category_4_column_index = "R"
    category_1_url_column_index = "S"
    category_2_url_index = "T"
    category_3_url_index = "U"
    category_4_url_index = "V"
    product_category_col_index = "W"
    referral_fee_percentage_col_index = "X"
    shipping_col_index = "Y"
    selling_price_column_index = "Z"
    label_fee_column_index = "AA"
    processing_fee_column_index = "AB"
    profit_loss_column_index = "AC"
    detail_columns_start_index = "AD"
    details_raw_column_index = "AE"


    return (sku_column_index, product_id_col_index, heading_col_index, brand_col_index, price_col_index, image_1_column_index, image_2_column_index, image_3_column_index, image_4_column_index, image_5_column_index, summary_column_index, key_feature_1_column_index, key_feature_2_column_index, remaining_key_features_column_index, category_1_column_index, category_2_column_index, category_3_column_index, category_4_column_index, category_1_url_column_index, category_2_url_index, category_3_url_index, category_4_url_index, product_category_col_index, referral_fee_percentage_col_index, shipping_col_index, selling_price_column_index, label_fee_column_index, processing_fee_column_index, profit_loss_column_index, detail_columns_start_index, details_raw_column_index)


# --- Part 6: Main Function ---
def main():
    logging.info("Script started.")
    client = authenticate_gspread()
    worksheet = get_worksheet(client)

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[["Excel Files", "*.xlsx"]])

    if not file_path:
        logging.warning("No file selected. Script will exit.")
        print("No file selected.")
        return

    logging.info(f"Selected file: {file_path}")
    try:
        df = load_excel(file_path)
        logging.info(f"Excel file '{file_path}' loaded successfully.")
    except FileNotFoundError:
        logging.error(f"Error: Excel file not found at '{file_path}'.")
        print(f"Error: Excel file not found at '{file_path}'.")
        return
    except Exception as e:
        logging.error(f"Error loading Excel file: {e}", exc_info=True)
        print(f"Error loading Excel file: {e}")
        return

    required_columns = ['web-scraper-order', 'web-scraper-start-url', 'heading', 'brand', 'market_price', 'images', 'images-src', 'summary', 'keyfeatures', 'specifications', 'shipping_status', 'pickup_status', 'delivery_status', 'categoryinfo', 'schema_org_product', 'schema_org_breadcrumbs', 'details']
    if not all(col in df.columns for col in required_columns):
        logging.error(f"Required columns not found in Excel file. Found columns: {df.columns.tolist()}")
        print("Required columns not found in the Excel file. Found columns:", df.columns.tolist())
        return

    df["product_id"] = df["web-scraper-start-url"].apply(extract_product_id)
    existing_product_ids = get_existing_product_ids(worksheet)

    updates = []
    new_rows = []

    (sku_column_index, product_id_col_index, heading_col_index, brand_col_index, price_col_index, image_1_column_index, image_2_column_index, image_3_column_index, image_4_column_index, image_5_column_index, summary_column_index, key_feature_1_column_index, key_feature_2_column_index, remaining_key_features_column_index, category_1_column_index, category_2_column_index, category_3_column_index, category_4_column_index, category_1_url_column_index, category_2_url_index, category_3_url_index, category_4_url_index, product_category_col_index, referral_fee_percentage_col_index, shipping_col_index, selling_price_column_index, label_fee_column_index, processing_fee_column_index, profit_loss_column_index, detail_columns_start_index, details_raw_column_index) = get_column_indices()


    header_row = worksheet.row_values(1)
    headers_to_update = {}
    if 'SKU' not in header_row:
        headers_to_update['A1'] = [['SKU']]
    if 'Product ID' not in header_row:
        headers_to_update['B1'] = [['Product ID']]
    if 'Heading' not in header_row:
        headers_to_update['C1'] = [['Heading']]
    if 'Brand' not in header_row:
        headers_to_update['D1'] = [['Brand']]
    if 'Price' not in header_row:
        headers_to_update['E1'] = [['Price']]
    if 'Image 1' not in header_row:
        for idx, col_header in enumerate([f'Image {i+1}' for i in range(IMAGE_COLUMN_COUNT)]):
            headers_to_update[f'{chr(ord("F") + idx)}1'] = [[col_header]]
    if 'Summary' not in header_row:
        headers_to_update['K1'] = [['Summary']]
    if 'Key Feature 1' not in header_row:
        headers_to_update['L1'] = [['Key Feature 1']]
    if 'Key Feature 2' not in header_row:
        headers_to_update['M1'] = [['Key Feature 2']]
    if 'Remaining Key Features' not in header_row:
        headers_to_update['N1'] = [['Remaining Key Features']]
    if 'Category 1' not in header_row:
        headers_to_update['O1'] = [['Category 1']]
    if 'Category 2' not in header_row:
        headers_to_update['P1'] = [['Category 2']]
    if 'Category 3' not in header_row:
        headers_to_update['Q1'] = [['Category 3']]
    if 'Category 4' not in header_row:
        headers_to_update['R1'] = [['Category 4']]
    if 'Category 1 URL' not in header_row:
        headers_to_update['S1'] = [['Category 1 URL']]
    if 'Category 2 URL' not in header_row:
        headers_to_update['T1'] = [['Category 2 URL']]
    if 'Category 3 URL' not in header_row:
        headers_to_update['U1'] = [['Category 3 URL']]
    if 'Category 4 URL' not in header_row:
        headers_to_update['V1'] = [['Category 4 URL']]
    if 'Product Category' not in header_row:
        headers_to_update['W1'] = [['Product Category']]
    if 'Referral Fee Percentage' not in header_row:
        headers_to_update['X1'] = [['Referral Fee Percentage']]
    if 'Shipping' not in header_row:
        headers_to_update['Y1'] = [['Shipping']]
    if 'Selling Price' not in header_row:
        headers_to_update['Z1'] = [['Selling Price']]
    if 'Label Fee' not in header_row:
        headers_to_update['AA1'] = [['Label Fee']]
    if 'Processing Fee' not in header_row:
        headers_to_update['AB1'] = [['Processing Fee']]
    if 'Profit/Loss' not in header_row:
        headers_to_update['AC1'] = [['Profit/Loss']]
    if 'Details' not in header_row: # Header for Column AD (processed data column)
        headers_to_update['AD1'] = [['Details']]
    if 'Details - Raw' not in header_row: # Header for Column AE (raw data column)
        headers_to_update['AE1'] = [['Details - Raw']]


    update_headers_sheet(worksheet, headers_to_update, batch_update_sheet)

    for index, row in df.iterrows():
        logging.info(f"Processing row {index + 2} (Product ID: {row.get('web-scraper-start-url', 'N/A')})...")

        # 1. Extract data using imported functions
        logging.info(f"  Row {index + 2}: Extracting product data...")
        product_id = extract_product_id(row['web-scraper-start-url'])
        numeric_price = extract_numeric_price(row['market_price'])
        image_urls = extract_images(row['images'])
        summary_text = extract_summary(row['heading'], row['summary'])
        key_feature_1, key_feature_2, remaining_key_features = extract_key_features(row['keyfeatures'], summary_text)
        category_names, category_urls = extract_categories(row['schema_org_breadcrumbs']) # Using corrected function
        product_category = get_product_category(category_names, category_urls, row['heading'], summary_text)
        referral_fee_percentage = calculate_referral_fee(product_category, DEFAULT_SELLING_PRICE)
        sku = f"{product_id}-{numeric_price if numeric_price is not None else 0}-PK-WMPL"
        details_text = row['details'] # Raw details text from Excel
        logging.info(f"  Row {index + 2}: Data extraction complete.")

        # 2. Log category data
        logging.info(f"  Row {index + 2}: Extracted Categories - Names: {category_names}, URLs: {category_urls}")

        # 3. Construct new_row_data
        logging.info(f"  Row {index + 2}: Constructing new_row_data list...")
        new_row_data = [
            sku,
            product_id,
            row['heading'],
            row['brand'],
            numeric_price,
            image_urls[0] if len(image_urls) > 0 else "",
            image_urls[1] if len(image_urls) > 1 else "",
            image_urls[2] if len(image_urls) > 2 else "",
            image_urls[3] if len(image_urls) > 3 else "",
            image_urls[4] if len(image_urls) > 4 else "",
            summary_text,
            key_feature_1,
            key_feature_2,
            remaining_key_features,
            category_names[0],
            category_names[1],
            category_names[2],
            category_names[3],
            category_urls[0],
            category_urls[1],
            category_urls[2],
            category_urls[3],
            product_category,
            referral_fee_percentage,
            "", # Shipping (Column Y) - Empty string initially
            DEFAULT_SELLING_PRICE, # Selling Price (Column Z) - Default value
            DEFAULT_LABEL_FEE, # Label Fee (Column AA) - Default value
            DEFAULT_PROCESSING_FEE, # Processing Fee (Column AB) - Default value
            "", # Profit/Loss (Column AC) - Empty string initially, formula applied later
            "", # Column AD - processed in Python now, will be populated below
            details_text # Raw details for Column AE
        ]
        logging.info(f"  Row {index + 2}: new_row_data list constructed.")

        # 4. Check if product_id exists
        logging.info(f"  Row {index + 2}: Checking if product ID '{product_id}' exists in Google Sheet...")
        if product_id and product_id in existing_product_ids:
            logging.info(f"  Row {index + 2}: Product ID '{product_id}' found in Google Sheet.")
            sheet_row = existing_product_ids[product_id]

            # 5. Prepare updates for existing product
            logging.info(f"  Row {index + 2}: Preparing updates for existing product in row {sheet_row}...")
            updates.append({'range': f"E{sheet_row}", 'values': [[numeric_price]]})
            updates.append({'range': f"F{sheet_row}", 'values': [[image_urls[0] if len(image_urls) > 0 else ""]]})
            updates.append({'range': f"G{sheet_row}", 'values': [[image_urls[1] if len(image_urls) > 1 else ""]]})
            updates.append({'range': f"H{sheet_row}", 'values': [[image_urls[2] if len(image_urls) > 2 else ""]]})
            updates.append({'range': f"I{sheet_row}", 'values': [[image_urls[3] if len(image_urls) > 3 else ""]]})
            updates.append({'range': f"J{sheet_row}", 'values': [[image_urls[4] if len(image_urls) > 4 else ""]]})
            updates.append({'range': f"AE{sheet_row}", 'values': [[details_text]]}) # Update raw details for existing rows too
            logging.info(f"  Row {index + 2}: Updates prepared for existing product.")

        else:
            logging.info(f"  Row {index + 2}: Product ID '{product_id}' not found in Google Sheet. Preparing to append as new row.")
            # 6. Append new_row_data to new_rows list
            logging.info(f"  Row {index + 2}: Appending new_row_data to new_rows list...")
            new_rows.append(new_row_data)
            logging.info(f"  Row {index + 2}: new_row_data appended to new_rows list.")
        logging.info(f"Processing for row {index + 2} complete.\n")


    # Sheet Update Operations:
    # 7. Append new_rows to sheet
    logging.info("Appending new rows to Google Sheet...")
    next_row_start = append_new_rows_sheet(worksheet, new_rows)
    if next_row_start:
        logging.info(f"New rows appended to sheet. Starting row: {next_row_start}. Now updating columns for new rows...")
        # 8. Call column update functions
        update_column_a_sheet(worksheet, sku_column_index, next_row_start, len(new_rows), new_rows)
        update_column_b_sheet(worksheet, product_id_col_index, next_row_start, len(new_rows), new_rows)
        update_column_c_sheet(worksheet, heading_col_index, next_row_start, len(new_rows), new_rows)
        update_column_d_sheet(worksheet, brand_col_index, next_row_start, len(new_rows), new_rows)
        update_column_e_sheet(worksheet, price_col_index, selling_price_column_index, referral_fee_percentage_col_index, label_fee_column_index, processing_fee_column_index, shipping_col_index, profit_loss_column_index, detail_columns_start_index, next_row_start, len(new_rows))
        update_columns_f_to_j_sheet(worksheet, image_1_column_index, image_2_column_index, image_3_column_index, image_4_column_index, image_5_column_index, next_row_start, len(new_rows), new_rows)
        update_column_k_sheet(worksheet, summary_column_index, next_row_start, len(new_rows), new_rows)
        update_column_l_sheet(worksheet, key_feature_1_column_index, next_row_start, len(new_rows), new_rows)
        update_column_m_sheet(worksheet, key_feature_2_column_index, next_row_start, len(new_rows), new_rows)
        update_column_n_sheet(worksheet, remaining_key_features_column_index, next_row_start, len(new_rows), new_rows)
        update_column_o_sheet(worksheet, category_1_column_index, next_row_start, len(new_rows), new_rows)
        update_column_p_sheet(worksheet, category_2_column_index, next_row_start, len(new_rows), new_rows)
        update_column_q_sheet(worksheet, category_3_column_index, next_row_start, len(new_rows), new_rows)
        update_column_r_sheet(worksheet, category_4_column_index, next_row_start, len(new_rows), new_rows)
        update_column_s_sheet(worksheet, category_1_url_column_index, next_row_start, len(new_rows), new_rows)
        update_column_t_sheet(worksheet, category_2_url_index, next_row_start, len(new_rows), new_rows)
        update_column_u_sheet(worksheet, category_3_url_index, next_row_start, len(new_rows), new_rows)
        update_column_v_sheet(worksheet, category_4_url_index, next_row_start, len(new_rows), new_rows)
        update_column_w_sheet(worksheet, product_category_col_index, next_row_start, len(new_rows), new_rows)
        update_column_x_sheet(worksheet, referral_fee_percentage_col_index, next_row_start, len(new_rows), new_rows)
        update_column_y_sheet(worksheet, shipping_col_index, next_row_start, len(new_rows), new_rows)
        update_column_z_sheet(worksheet, selling_price_column_index, next_row_start, len(new_rows), new_rows)
        update_column_aa_sheet(worksheet, label_fee_column_index, next_row_start, len(new_rows), new_rows)
        update_column_ab_sheet(worksheet, processing_fee_column_index, next_row_start, len(new_rows), new_rows)
        update_column_ac_sheet(worksheet, profit_loss_column_index, shipping_col_index, selling_price_column_index, price_col_index, label_fee_column_index, processing_fee_column_index, next_row_start, len(new_rows))
        update_column_ad_sheet(worksheet, detail_columns_start_index, next_row_start, len(new_rows), new_rows) # Updates Column AD with processed data from Python
        update_column_ae_sheet(worksheet, details_raw_column_index, next_row_start, len(new_rows), new_rows) # Updates Column AE with raw data
        logging.info("Column updates for new rows completed.")
    else:
        logging.info("No new rows to append, skipping column updates.")


    # 9. Batch update for existing products
    if updates:
        logging.info("Applying batch updates for existing products...")
        batch_update_sheet(worksheet, updates)
        logging.info("Batch updates for existing products applied.")

    logging.info("Google Sheet updated successfully (Modular Columns & Extraction Code).")
    print("Google Sheet updated successfully (Modular Columns & Extraction Code).")
    logging.info("Script finished.")

if __name__ == '__main__':
    main()