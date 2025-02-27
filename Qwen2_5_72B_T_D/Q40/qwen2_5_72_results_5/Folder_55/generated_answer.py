def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_75 = sorted_chars[:75]
    return sorted(smallest_75, key=ord, reverse=True)