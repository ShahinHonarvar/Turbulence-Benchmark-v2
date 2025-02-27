def return_n_greatest_chars(s):
    n = 36
    return sorted(s, reverse=True)[:n]