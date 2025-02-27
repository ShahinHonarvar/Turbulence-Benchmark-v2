def return_nth_smallest_ascii(input_string):
    extracted_chars = input_string[14:36]
    sorted_chars = sorted(extracted_chars)
    return sorted_chars[10]