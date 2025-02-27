def return_n_smallest_chars(s):
    sorted_chars_desc = sorted(s, reverse=True)
    return sorted_chars_desc[:28]