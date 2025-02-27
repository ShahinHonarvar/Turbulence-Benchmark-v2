def return_n_greatest_chars(s):
    if not s:
        return []
    return sorted(s, reverse=True)[:23]