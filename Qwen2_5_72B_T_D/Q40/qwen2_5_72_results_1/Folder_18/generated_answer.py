def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=ord)
    smallest_52 = sorted_s[:52]
    return sorted(smallest_52, key=ord, reverse=True)