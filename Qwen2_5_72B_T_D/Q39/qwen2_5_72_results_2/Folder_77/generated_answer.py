def return_n_greatest_chars(s):
    s_sorted = sorted(s, key=ord)
    return s_sorted[-47:]