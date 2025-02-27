def return_n_greatest_chars(s):
    unique_chars = sorted(set(s))
    if len(unique_chars) <= 29:
        return unique_chars
    else:
        return sorted(set(unique_chars[-29:]))