def return_n_greatest_chars(s):
    sorted_chars = sorted(s)
    greatest_chars = sorted_chars[-45:]
    return greatest_chars