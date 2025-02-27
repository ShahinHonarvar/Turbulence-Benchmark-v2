def return_n_smallest_chars(s):
    unique_chars = sorted(list(set(s)))
    smallest_chars_desc = sorted(unique_chars[:11], reverse=True)
    return smallest_chars_desc