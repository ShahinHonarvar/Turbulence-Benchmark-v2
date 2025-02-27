def return_n_greatest_chars(s):
    if len(s) <= 58:
        return sorted(s)
    return sorted(s)[-58:]