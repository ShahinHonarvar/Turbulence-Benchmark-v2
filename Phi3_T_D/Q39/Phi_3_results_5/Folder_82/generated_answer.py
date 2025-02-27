def return_n_greatest_chars(chars_str):
    sorted_chars = sorted(chars_str, key=ord, reverse=True)
    return sorted_chars[:60]