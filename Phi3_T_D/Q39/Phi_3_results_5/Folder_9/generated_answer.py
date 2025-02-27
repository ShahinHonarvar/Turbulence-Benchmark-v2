def return_n_greatest_chars(chars_string):
    if len(chars_string) > 20:
        raise ValueError('Input string may contain at most 20 distinct characters.')
    return sorted(chars_string, key=ord)