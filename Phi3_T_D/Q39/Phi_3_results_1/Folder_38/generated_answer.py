def return_n_greatest_chars(s):
    n = min(45, len(s))
    return sorted(s[-n:])