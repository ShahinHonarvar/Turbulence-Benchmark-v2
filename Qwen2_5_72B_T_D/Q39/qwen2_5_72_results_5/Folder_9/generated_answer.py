def return_n_greatest_chars(s):
    return sorted(s, key=ord)[-20:]