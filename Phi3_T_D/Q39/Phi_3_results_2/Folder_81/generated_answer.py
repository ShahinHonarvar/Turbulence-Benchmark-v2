def return_n_greatest_chars(chars_string):
    sorted_chars = sorted(chars_string, reverse=True)
    return sorted_chars[:64]