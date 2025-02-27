def return_n_greatest_chars(s):
    max_chars = sorted(s, reverse=True)[:46]
    return max_chars