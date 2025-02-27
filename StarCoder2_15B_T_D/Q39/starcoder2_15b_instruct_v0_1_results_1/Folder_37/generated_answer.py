def return_n_greatest_chars(chars_str):
    if len(chars_str) < 26:
        raise ValueError('The input string must have at least 26 distinct characters.')
    sorted_chars = sorted(chars_str, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:26]