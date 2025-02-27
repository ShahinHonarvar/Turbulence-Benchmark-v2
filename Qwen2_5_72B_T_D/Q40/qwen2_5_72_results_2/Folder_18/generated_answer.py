def return_n_smallest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:52]
    return sorted_chars