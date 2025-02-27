def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_47 = sorted_chars[:47]
    return sorted(smallest_47, key=ord, reverse=True)