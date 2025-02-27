def return_n_smallest_chars(string):
    smallest_chars = sorted(string, key=ord)[:49]
    return sorted(smallest_chars, key=ord, reverse=True)