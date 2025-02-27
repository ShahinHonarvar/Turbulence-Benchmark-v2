def return_n_greatest_chars(s):
    greatest_chars = sorted(s)[-60:]
    return greatest_chars[::-1]