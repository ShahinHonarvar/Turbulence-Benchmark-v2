def return_n_smallest_chars(s):
    distinct_chars = sorted(set(s), key=ord)[:26]
    return sorted(distinct_chars, reverse=True)