def return_n_greatest_chars(s):
    sorted_s = sorted(s)
    greatest_chars = sorted_s[-48:]
    return greatest_chars