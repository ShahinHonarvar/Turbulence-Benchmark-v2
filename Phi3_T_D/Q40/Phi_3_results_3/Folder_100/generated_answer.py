def return_n_smallest_chars(distinct_string):
    smallest_chars = sorted(distinct_string)[:72]
    smallest_chars.reverse()
    return smallest_chars