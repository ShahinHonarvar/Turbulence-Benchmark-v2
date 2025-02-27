def return_n_greatest_chars(chars):
    if not chars or len(chars) > 38:
        return []
    return sorted(chars, reverse=True)[:38]