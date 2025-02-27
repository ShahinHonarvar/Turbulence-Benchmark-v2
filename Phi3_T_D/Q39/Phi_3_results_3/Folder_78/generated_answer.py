def return_n_greatest_chars(s):
    n = 43
    return sorted(list(s), reverse=True)[:n]