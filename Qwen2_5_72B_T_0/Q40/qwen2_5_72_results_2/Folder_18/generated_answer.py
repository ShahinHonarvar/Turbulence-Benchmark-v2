def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_52 = sorted_chars[:52]
    return sorted(smallest_52, key=ord, reverse=True)