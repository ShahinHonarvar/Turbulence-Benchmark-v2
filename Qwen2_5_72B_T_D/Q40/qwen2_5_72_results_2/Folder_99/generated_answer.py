def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_35 = sorted_chars[:35]
    return sorted(smallest_35, key=ord, reverse=True)