def return_n_greatest_chars(s):
    unique_chars = sorted(set(s), reverse=True)[:21]
    return sorted(unique_chars)