def return_n_greatest_chars(s):
    chars = sorted(set(s), key=ord, reverse=True)
    return chars[:27]