def return_n_greatest_chars(s):
    return sorted(s)[-40:] if len(s) > 40 else sorted(s)