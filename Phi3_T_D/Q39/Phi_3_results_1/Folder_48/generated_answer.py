def return_n_greatest_chars(s):
    n = 12
    return sorted(list(s), key=ord)[-n:]