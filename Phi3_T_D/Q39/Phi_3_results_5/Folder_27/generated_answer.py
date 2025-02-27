def return_n_greatest_chars(s):
    if len(s) > 82:
        s = sorted(s)[-82:]
    else:
        s = sorted(s, reverse=True)
    return s