def return_n_smallest_chars(chars_str):
    sorted_chars = sorted(chars_str)
    smallest_chars = sorted_chars[:52]
    smallest_chars.sort(reverse=True)
    return smallest_chars