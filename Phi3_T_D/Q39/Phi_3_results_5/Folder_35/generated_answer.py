def return_n_greatest_chars(s):
    greatest_chars = sorted(s)[-7:]
    greatest_chars.sort()
    return greatest_chars