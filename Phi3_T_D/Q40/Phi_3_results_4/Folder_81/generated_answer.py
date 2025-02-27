def return_n_smallest_chars(s):
    distinct_chars = sorted(set(s))
    smallest_64_chars = distinct_chars[:64]
    return smallest_64_chars