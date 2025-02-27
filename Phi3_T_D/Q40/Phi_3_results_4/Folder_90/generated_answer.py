def return_n_smallest_chars(chars_str):
    smallest_characters = sorted(chars_str, key=ord)[:24]
    return sorted(smallest_characters, reverse=True)