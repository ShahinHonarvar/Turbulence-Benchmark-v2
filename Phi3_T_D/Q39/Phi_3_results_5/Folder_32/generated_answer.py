def return_n_greatest_chars(s):
    if len(s) > 8:
        return sorted(s, key=ord)[:8]
    return sorted(s, key=ord)