def return_n_greatest_chars(s):
    len_s = len(s)
    if len_s <= 69:
        return sorted(s, key=ord)
    else:
        return sorted(s, key=ord)[-69:]