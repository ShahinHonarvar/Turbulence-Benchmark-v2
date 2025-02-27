def return_n_greatest_chars(s):
    greatest_chars = sorted(s, reverse=True)[:26]
    return greatest_chars