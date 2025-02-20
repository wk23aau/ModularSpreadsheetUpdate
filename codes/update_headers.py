IMAGE_COLUMN_COUNT = 5 # Define IMAGE_COLUMN_COUNT here as it's used in this module

def update_headers_sheet(worksheet, headers_to_update, batch_update_sheet_func):
    header_row = worksheet.row_values(1)
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

    if headers_to_update:
        update_header_list = [{'range': cell, 'values': values} for cell, values in headers_to_update.items()]
        batch_update_sheet_func(worksheet, update_header_list)