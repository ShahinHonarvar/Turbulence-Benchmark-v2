def return_n_greatest_chars(s):
    if len(s) < 31:
        sorted_chars = sorted(s)
    else:
        sorted_chars = sorted(s)[-31:]
    return sorted_chars