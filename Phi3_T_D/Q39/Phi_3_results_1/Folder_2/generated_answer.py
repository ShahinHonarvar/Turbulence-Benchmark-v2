def return_n_greatest_chars(s):
    if len(s) < 48:
        return []
    return sorted(s, key=ord, reverse=True)[:48]