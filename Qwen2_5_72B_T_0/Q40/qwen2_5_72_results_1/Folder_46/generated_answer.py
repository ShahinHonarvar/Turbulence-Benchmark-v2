def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_54 = sorted_chars[:54]
    return sorted(smallest_54, key=ord, reverse=True)