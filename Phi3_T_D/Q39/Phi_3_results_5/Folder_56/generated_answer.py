def return_n_greatest_chars(chars_str):
    if len(chars_str) != 21:
        raise ValueError('Input string must contain exactly 21 distinct characters.')
    sorted_list = sorted(chars_str, reverse=True)
    return sorted_list