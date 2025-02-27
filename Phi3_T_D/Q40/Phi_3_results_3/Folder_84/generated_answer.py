def return_n_smallest_chars(string):
    distinct_chars = sorted(set(string))
    return sorted(distinct_chars[:10])