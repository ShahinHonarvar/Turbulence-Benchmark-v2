def return_n_smallest_chars(s):
    distinguised_chars = distinct_sorted = sorted(set(s))
    return_sorted = sorted(distinguised_chars, reverse=True)[:33]
    return return_sorted