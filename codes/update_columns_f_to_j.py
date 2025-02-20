def update_columns_f_to_j_sheet(worksheet, image_1_column_index, image_2_column_index, image_3_column_index, image_4_column_index, image_5_column_index, start_row, num_rows, new_rows):
    image_1_range = f"{image_1_column_index}{str(start_row)}:{image_1_column_index}{str(start_row + num_rows - 1)}" # Column F - Image 1
    image_1_values = [[row[5]] for row in new_rows] # Image 1 is the 6th element in new_rows
    worksheet.update(image_1_range, image_1_values)

    image_2_range = f"{image_2_column_index}{str(start_row)}:{image_2_column_index}{str(start_row + num_rows - 1)}" # Column G - Image 2
    image_2_values = [[row[6]] for row in new_rows] # Image 2 is the 7th element in new_rows
    worksheet.update(image_2_range, image_2_values)

    image_3_range = f"{image_3_column_index}{str(start_row)}:{image_3_column_index}{str(start_row + num_rows - 1)}" # Column H - Image 3
    image_3_values = [[row[7]] for row in new_rows] # Image 3 is the 8th element in new_rows
    worksheet.update(image_3_range, image_3_values)

    image_4_range = f"{image_4_column_index}{str(start_row)}:{image_4_column_index}{str(start_row + num_rows - 1)}" # Column I - Image 4
    image_4_values = [[row[8]] for row in new_rows] # Image 4 is the 9th element in new_rows
    worksheet.update(image_4_range, image_4_values)

    image_5_range = f"{image_5_column_index}{str(start_row)}:{image_5_column_index}{str(start_row + num_rows - 1)}" # Column J - Image 5
    image_5_values = [[row[9]] for row in new_rows] # Image 5 is the 10th element in new_rows
    worksheet.update(image_5_range, image_5_values)