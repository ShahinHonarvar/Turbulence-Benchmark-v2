def return_n_greatest_chars(string):
    chars = sorted(string, key=ord)
    return chars[:12]