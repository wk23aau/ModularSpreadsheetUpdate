def extract_details_keyword_grouped(details_text):
    extracted_values = []
    start_index = 0
    while True:
        start_keyword_index = details_text.find('{"details":"', start_index)
        if start_keyword_index == -1:
            break

        value_start_index = start_keyword_index + len('{"details":"')
        value_end_index = details_text.find('"}', value_start_index)

        if value_end_index != -1:
            value = details_text[value_start_index:value_end_index]
            extracted_values.append(value)
            start_index = value_end_index + len('"}')
        else:
            break

    output_dict = {"AD values": []}
    value_pairs = []
    for index, value in enumerate(extracted_values):
        value_pairs.append(value)
        if (index + 1) % 2 == 0:
            output_dict["AD values"].append(value_pairs)
            value_pairs = []
    if value_pairs:
        output_dict["AD values"].append(value_pairs)

    return output_dict