def return_nth_smallest_ascii(string):
    chars = list(string)
    chars.sort(key=ord)
    extracted_chars = chars[17:35]
    return extracted_chars[17]