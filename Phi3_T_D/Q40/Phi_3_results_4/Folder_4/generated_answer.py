def return_n_smallest_chars(distinct_chars):
    smallest_chars = sorted(distinct_chars)[:90]
    return sorted(smallest_chars, reverse=True)