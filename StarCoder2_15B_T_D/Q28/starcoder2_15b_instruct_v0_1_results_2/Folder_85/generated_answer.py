def return_nth_smallest_ascii(string):
    extracted_chars = [char for char in string[17:87]]
    sorted_chars = sorted(extracted_chars)
    return sorted_chars[14]