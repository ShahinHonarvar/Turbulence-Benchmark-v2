def return_nth_smallest_ascii(string):
    extracted_chars = string[0:87]
    sorted_chars = sorted(extracted_chars)
    return sorted_chars[13]