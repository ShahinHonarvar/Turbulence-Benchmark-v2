def return_n_smallest_chars(s):
    unique_sorted = sorted(set(s), key=ord)
    return unique_sorted[:26][::-1]