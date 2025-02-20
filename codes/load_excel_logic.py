import pandas as pd # Import pandas here as it's used in this module

def load_excel(file_path):
    df = pd.read_excel(file_path, dtype=str)
    df.columns = df.columns.str.strip().str.lower()
    print("Columns read from Excel:", df.columns.tolist())
    return df