def return_n_greatest_chars(s):
    greatest_chars = sorted(s, reverse=True)[:83]
    return greatest_chars