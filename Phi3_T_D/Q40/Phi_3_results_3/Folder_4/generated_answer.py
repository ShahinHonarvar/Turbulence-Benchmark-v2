def return_n_smallest_chars(string):
    unique_chars = sorted(set(string))
    smallest_chars = unique_chars[:90]
    return sorted(smallest_chars, reverse=True)