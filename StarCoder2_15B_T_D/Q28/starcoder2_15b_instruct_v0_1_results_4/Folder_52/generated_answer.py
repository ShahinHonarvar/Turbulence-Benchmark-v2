def return_nth_smallest_ascii(string):
    extracted_chars = [char for char in string[46:73]]
    sorted_chars = sorted(extracted_chars)
    return sorted_chars[14]