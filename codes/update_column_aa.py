DEFAULT_LABEL_FEE = 4.5 # Define DEFAULT_LABEL_FEE here as it's used in this module

def update_column_aa_sheet(worksheet, label_fee_column_index, start_row, num_rows, new_rows):
    label_fee_range = f"{label_fee_column_index}{str(start_row)}:{label_fee_column_index}{str(start_row + num_rows - 1)}"
    worksheet.format(label_fee_range, {"numberFormat": {"type": "NUMBER", "pattern": "#,##0.00"}})
    worksheet.update(label_fee_range, [[DEFAULT_LABEL_FEE]] * num_rows)