import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import tkinter as tk
from tkinter import filedialog

# Import column update functions from separate files
from update_headers import update_headers_sheet
from update_column_a import update_column_a_sheet  # SKU
from update_column_b import update_column_b_sheet  # Product ID
from update_column_c import update_column_c_sheet  # Heading
from update_column_d import update_column_d_sheet  # Brand
from update_column_e import update_column_e_sheet  # Price
from update_columns_f_to_j import update_columns_f_to_j_sheet # Image 1-5 (Columns F-J)
from update_column_k import update_column_k_sheet  # Summary
from update_column_l import update_column_l_sheet  # Key Feature 1
from update_column_m import update_column_m_sheet  # Key Feature 2
from update_column_n import update_column_n_sheet  # Remaining Key Features
from update_column_o import update_column_o_sheet  # Category 1
from update_column_p import update_column_p_sheet  # Category 2
from update_column_q import update_column_q_sheet  # Category 3
from update_column_r import update_column_r_sheet  # Category 4
from update_column_s import update_column_s_sheet  # Category 1 URL
from update_column_t import update_column_t_sheet  # Category 2 URL
from update_column_u import update_column_u_sheet  # Category 3 URL
from update_column_v import update_column_v_sheet  # Category 4 URL
from update_column_w import update_column_w_sheet  # Product Category
from update_column_x import update_column_x_sheet  # Referral Fee Percentage
from update_column_y import update_column_y_sheet  # Shipping
from update_column_z import update_column_z_sheet  # Selling Price
from update_column_aa import update_column_aa_sheet # Label Fee
from update_column_ab import update_column_ab_sheet # Processing Fee
from update_column_ac import update_column_ac_sheet # Profit/Loss
from update_column_ad import update_column_ad_sheet # Details

# Import extraction logic from separate files
from extract_images_logic import extract_images
from extract_summary_logic import extract_summary
from extract_key_features_logic import extract_key_features
from extract_categories_logic import extract_categories
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


# --- Part 4: Google Sheets Interaction ---
def authenticate_gspread(creds_path=CREDENTIALS_FILE):
    creds = Credentials.from_service_account_file(creds_path, scopes=SCOPES)
    return gspread.authorize(creds)

def get_worksheet(client, sheet_id=SPREADSHEET_ID, sheet_index=0):
    sheet = client.open_by_key(sheet_id)
    return sheet.get_worksheet(sheet_index)

def get_existing_product_ids(worksheet):
    existing_data = worksheet.get_all_values()
    return {row[1].strip(): idx + 1 for idx, row in enumerate(existing_data) if len(row) > 1}

def batch_update_sheet(worksheet, updates):
    if updates:
        worksheet.batch_update(updates)

def append_new_rows_sheet(worksheet, new_rows): # Simplified append_new_rows_sheet
    if new_rows:
        next_row = len(worksheet.get_all_values()) + 1
        rows_to_insert = [row[:-1] for row in new_rows]
        worksheet.insert_rows(rows_to_insert, row=next_row)
        return next_row # Return next_row for column updates to use


# --- Part 5: Column Indexing ---
def get_column_indices():
    selling_price_column_index = "Z"
    referral_fee_column_index = "X"
    product_category_column_index = "W"
    shipping_column_index = "Y"
    label_fee_column_index = "AA"
    processing_fee_column_index = "AB"
    profit_loss_column_index = "AC"
    sku_column_index = "A"
    detail_columns_start_index = "AD"
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
    price_col_index = "E"
    brand_col_index = "D"
    heading_col_index = "C"
    product_id_col_index = "B"


    return (sku_column_index, product_id_col_index, heading_col_index, brand_col_index, price_col_index, image_1_column_index, image_2_column_index, image_3_column_index, image_4_column_index, image_5_column_index, summary_column_index, key_feature_1_column_index, key_feature_2_column_index, remaining_key_features_column_index, category_1_column_index, category_2_column_index, category_3_column_index, category_4_column_index, category_1_url_column_index, category_2_url_index, category_3_url_index, category_4_url_index, product_category_col_index, referral_fee_percentage_col_index, shipping_col_index, selling_price_column_index, label_fee_column_index, processing_fee_column_index, profit_loss_column_index, detail_columns_start_index)


# --- Part 6: Main Function ---
def main():
    client = authenticate_gspread()
    worksheet = get_worksheet(client)

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select Excel File", filetypes=[["Excel Files", "*.xlsx"]])

    if not file_path:
        print("No file selected.")
        return

    try:
        df = load_excel(file_path) # Use imported load_excel function
    except FileNotFoundError:
        print(f"Error: Excel file not found at '{file_path}'.")
        return
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return

    required_columns = ['web-scraper-order', 'web-scraper-start-url', 'heading', 'brand', 'market_price', 'images', 'images-src', 'summary', 'keyfeatures', 'specifications', 'shipping_status', 'pickup_status', 'delivery_status', 'categoryinfo', 'schema_org_product', 'schema_org_breadcrumbs', 'categoryid', 'details']
    if not all(col in df.columns for col in required_columns):
        print("Required columns not found in the Excel file. Found columns:", df.columns.tolist())
        return

    df["product_id"] = df["web-scraper-start-url"].apply(extract_product_id) # Use imported extract_product_id
    existing_product_ids = get_existing_product_ids(worksheet)

    updates = []
    new_rows = []

    (sku_column_index, product_id_col_index, heading_col_index, brand_col_index, price_col_index, image_1_column_index, image_2_column_index, image_3_column_index, image_4_column_index, image_5_column_index, summary_column_index, key_feature_1_column_index, key_feature_2_column_index, remaining_key_features_column_index, category_1_column_index, category_2_column_index, category_3_column_index, category_4_column_index, category_1_url_column_index, category_2_url_index, category_3_url_index, category_4_url_index, product_category_col_index, referral_fee_percentage_col_index, shipping_col_index, selling_price_column_index, label_fee_column_index, processing_fee_column_index, profit_loss_column_index, detail_columns_start_index) = get_column_indices()


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
    if 'Details' not in header_row:
        headers_to_update['AD1'] = [['Details']]

    update_headers_sheet(worksheet, headers_to_update, batch_update_sheet) # Call header update function


    for _, row in df.iterrows():
        product_id = extract_product_id(row['web-scraper-start-url']) # Use imported extract_product_id
        numeric_price = extract_numeric_price(row['market_price']) # Use imported extract_numeric_price
        selling_price = DEFAULT_SELLING_PRICE
        referral_fee_percentage_default = DEFAULT_REFERRAL_FEE
        image_urls = extract_images(row['images']) # Use imported extract_images
        summary_text = extract_summary(row['heading'], row['summary']) # Use imported extract_summary
        key_feature_1, key_feature_2, remaining_key_features = extract_key_features(row['keyfeatures'], summary_text) # Use imported extract_key_features
        category_names, category_urls = extract_categories(row['schema_org_product']) # Use imported extract_categories
        product_category = get_product_category(category_names, category_urls, row['heading'], summary_text) # Use imported get_product_category
        referral_fee_percentage = calculate_referral_fee(product_category, selling_price) # Use imported calculate_referral_fee
        sku = f"{product_id}-{numeric_price if numeric_price is not None else 0}-PK-WMPL"
        details_text = row['details']

        new_row_data = [ # Data for initial row insertion
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
            "", # Shipping
            selling_price, # Selling Price
            DEFAULT_LABEL_FEE, # Label Fee
            DEFAULT_PROCESSING_FEE, # Processing Fee
            "=SUM(Y{0}+Z{0})-SUM(E{0}+AA{0}+AB{0})", # Profit/Loss formula
            details_text # Details
        ]

        if product_id and product_id in existing_product_ids:
            # For existing products, create updates for price and images (still in main)
            sheet_row = existing_product_ids[product_id]
            updates.append({'range': f"E{sheet_row}", 'values': [[numeric_price]]}) # Price Update
            updates.append({'range': f"F{sheet_row}", 'values': [[image_urls[0] if len(image_urls) > 0 else ""]]}) # Image 1 Update
            updates.append({'range': f"G{sheet_row}", 'values': [[image_urls[1] if len(image_urls) > 1 else ""]]}) # Image 2 Update
            updates.append({'range': f"H{sheet_row}", 'values': [[image_urls[2] if len(image_urls) > 2 else ""]]}) # Image 3 Update
            updates.append({'range': f"I{sheet_row}", 'values': [[image_urls[3] if len(image_urls) > 3 else ""]]}) # Image 4 Update
            updates.append({'range': f"J{sheet_row}", 'values': [[image_urls[4] if len(image_urls) > 4 else ""]]}) # Image 5 Update
        else:
            new_rows.append(new_row_data)


    next_row_start = append_new_rows_sheet(worksheet, new_rows) # Insert new rows and get start row

    if next_row_start: # Update columns for newly added rows
        update_column_a_sheet(worksheet, sku_column_index, next_row_start, len(new_rows), new_rows) # SKU (Column A)
        update_column_b_sheet(worksheet, product_id_col_index, next_row_start, len(new_rows), new_rows) # Product ID (Column B)
        update_column_c_sheet(worksheet, heading_col_index, next_row_start, len(new_rows), new_rows) # Heading (Column C)
        update_column_d_sheet(worksheet, brand_col_index, next_row_start, len(new_rows), new_rows) # Brand (Column D)
        update_column_e_sheet(worksheet, price_col_index, selling_price_column_index, referral_fee_percentage_col_index, label_fee_column_index, processing_fee_column_index, shipping_col_index, profit_loss_column_index, detail_columns_start_index, next_row_start, len(new_rows)) # Price, Selling Price, Fees, Profit/Loss (Column E, Z, AA, AB, Y, AC) - Combined for formula dependencies
        update_columns_f_to_j_sheet(worksheet, image_1_column_index, image_2_column_index, image_3_column_index, image_4_column_index, image_5_column_index, next_row_start, len(new_rows), new_rows) # Images 1-5 (Columns F-J)
        update_column_k_sheet(worksheet, summary_column_index, next_row_start, len(new_rows), new_rows) # Summary (Column K)
        update_column_l_sheet(worksheet, key_feature_1_column_index, next_row_start, len(new_rows), new_rows) # Key Feature 1 (Column L)
        update_column_m_sheet(worksheet, key_feature_2_column_index, next_row_start, len(new_rows), new_rows) # Key Feature 2 (Column M)
        update_column_n_sheet(worksheet, remaining_key_features_column_index, next_row_start, len(new_rows), new_rows) # Remaining Key Features (Column N)
        update_column_o_sheet(worksheet, category_1_column_index, next_row_start, len(new_rows), new_rows) # Category 1 (Column O)
        update_column_p_sheet(worksheet, category_2_column_index, next_row_start, len(new_rows), new_rows) # Category 2 (Column P)
        update_column_q_sheet(worksheet, category_3_column_index, next_row_start, len(new_rows), new_rows) # Category 3 (Column Q)
        update_column_r_sheet(worksheet, category_4_column_index, next_row_start, len(new_rows), new_rows) # Category 4 (Column R)
        update_column_s_sheet(worksheet, category_1_url_column_index, next_row_start, len(new_rows), new_rows) # Category 1 URL (Column S)
        update_column_t_sheet(worksheet, category_2_url_index, next_row_start, len(new_rows), new_rows) # Category 2 URL (Column T)
        update_column_u_sheet(worksheet, category_3_url_index, next_row_start, len(new_rows), new_rows) # Category 3 URL (Column U)
        update_column_v_sheet(worksheet, category_4_url_index, next_row_start, len(new_rows), new_rows) # Category 4 URL (Column V)
        update_column_w_sheet(worksheet, product_category_col_index, next_row_start, len(new_rows), new_rows) # Product Category (Column W)
        update_column_x_sheet(worksheet, referral_fee_percentage_col_index, next_row_start, len(new_rows), new_rows) # Referral Fee Percentage (Column X)
        update_column_y_sheet(worksheet, shipping_col_index, next_row_start, len(new_rows), new_rows) # Shipping (Column Y)
        update_column_z_sheet(worksheet, selling_price_column_index, next_row_start, len(new_rows), new_rows) # Selling Price (Column Z)
        update_column_aa_sheet(worksheet, label_fee_column_index, next_row_start, len(new_rows), new_rows) # Label Fee (Column AA)
        update_column_ab_sheet(worksheet, processing_fee_column_index, next_row_start, len(new_rows), new_rows) # Processing Fee (Column AB)
        update_column_ac_sheet(worksheet, profit_loss_column_index, shipping_col_index, selling_price_column_index, price_col_index, label_fee_column_index, processing_fee_column_index, next_row_start, len(new_rows)) # Profit/Loss (Column AC)
        update_column_ad_sheet(worksheet, detail_columns_start_index, next_row_start, len(new_rows), new_rows) # Details (Column AD)


    if updates:
        batch_update_sheet(worksheet, updates) # Update existing product prices and images

    print("Google Sheet updated successfully (Modular Columns & Extraction Code).")


if __name__ == '__main__':
    main()