DEFAULT_PROCESSING_FEE = 0.5 # Define DEFAULT_PROCESSING_FEE here as it's used in this module

def update_column_ab_sheet(worksheet, processing_fee_column_index, start_row, num_rows, new_rows):
    processing_fee_range = f"{processing_fee_column_index}{str(start_row)}:{processing_fee_column_index}{str(start_row + num_rows - 1)}"
    worksheet.format(processing_fee_range, {"numberFormat": {"type": "NUMBER", "pattern": "#,##0.00"}})
    worksheet.update(processing_fee_range, [[DEFAULT_PROCESSING_FEE]] * num_rows)