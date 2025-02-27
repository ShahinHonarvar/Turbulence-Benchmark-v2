def return_n_greatest_chars(s):
    if len(s) >= 11:
        n = 11
    else:
        n = len(s)
    greatest_chars = sorted(s)[-n:].sort()
    return greatest_chars