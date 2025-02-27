def return_n_smallest_chars(s):
    unique_sorted_chars = sorted(set(s), key=ord)
    return list(reversed(unique_sorted_chars[:27]))