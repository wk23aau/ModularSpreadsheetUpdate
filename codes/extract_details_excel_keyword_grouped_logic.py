import pandas as pd # Import pandas here as it's used in this module
from extract_details_keyword_grouped_logic import extract_details_keyword_grouped # Import extract_details_keyword_grouped

def extract_details_excel_keyword_grouped(excel_file):
    df = pd.read_excel(excel_file)
    extracted_data_dict = {}

    for index, row in df.iterrows():
        details_text = row['details']
        if not isinstance(details_text, str) or not details_text:
            continue

        row_output = extract_details_keyword_grouped(details_text)
        extracted_data_dict[index] = row_output

    return extracted_data_dict