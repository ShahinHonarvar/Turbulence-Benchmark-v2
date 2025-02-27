def return_n_greatest_chars(s):
    if len(s) < 52:
        return sorted(list(s), reverse=True)
    return sorted(list(s), reverse=True)[:52]