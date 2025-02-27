def return_n_smallest_chars(s):
    distinct_chars = list(set(s))
    smallest_chars = sorted(distinct_chars)[:76]
    return smallest_chars