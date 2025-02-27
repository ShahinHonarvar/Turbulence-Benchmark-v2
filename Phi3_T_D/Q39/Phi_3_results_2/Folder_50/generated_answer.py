def return_n_greatest_chars(s):
    distinct_chars = sorted(set(s), reverse=True)
    return distinct_chars[:16]