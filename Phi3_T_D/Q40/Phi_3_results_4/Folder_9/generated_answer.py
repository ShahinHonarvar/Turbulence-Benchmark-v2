def return_n_smallest_chars(chars_str):
    if len(set(chars_str)) < 20:
        raise ValueError('Not enough distinct characters')
    smallest_chars = sorted(chars_str)[:20]
    return smallest_chars