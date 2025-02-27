def return_n_smallest_chars(s):
    unique_chars = sorted(set(s), reverse=True)
    return unique_chars[:79]