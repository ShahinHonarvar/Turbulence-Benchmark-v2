def return_n_greatest_chars(s):
    return sorted(sorted(s, key=lambda x: x, reverse=True)[:83], key=lambda x: x)