def return_n_smallest_chars(chars_string):
    return sorted(chars_string, key=ord, reverse=True)[:32]