def return_n_greatest_chars(s):
    distinct_chars = sorted(set(s), reverse=True)[:14]
    return sorted(distinct_chars)