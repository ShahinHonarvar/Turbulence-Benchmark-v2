def return_n_greatest_chars(s):
    n = min(len(s), 69)
    return sorted(s)[-n:][::-1]