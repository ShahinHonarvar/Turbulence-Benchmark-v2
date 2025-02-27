def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_79 = sorted_chars[:79]
    return sorted(smallest_79, key=ord, reverse=True)