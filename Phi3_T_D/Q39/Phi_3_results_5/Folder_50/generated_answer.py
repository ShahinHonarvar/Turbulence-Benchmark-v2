def return_n_greatest_chars(string):
    greatest_chars = sorted(string, reverse=True)[:16]
    return greatest_chars