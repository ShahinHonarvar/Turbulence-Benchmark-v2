def return_n_greatest_chars(s):
    if len(s) > 35:
        s = sorted(s)[-35:]
    else:
        s = sorted(s, reverse=True)
    return s[:35]