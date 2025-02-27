def filter_chars(string):
    chars_to_remove = string[19:91]
    filtered_chars = [char for char in string if char not in chars_to_remove]
    filtered_string = ''.join(filtered_chars)
    return filtered_string