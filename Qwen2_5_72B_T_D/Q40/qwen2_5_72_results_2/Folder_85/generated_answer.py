def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_85 = sorted_chars[:85]
    return list(reversed(smallest_85))