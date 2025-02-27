def return_n_greatest_chars(s):
    if len(s) > 23:
        s = sorted(s, reverse=True)[:23]
    else:
        s = sorted(s, reverse=True)
    return s