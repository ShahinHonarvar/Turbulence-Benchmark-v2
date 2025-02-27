def return_n_greatest_chars(chars):
    if len(chars) < 13:
        return sorted(chars, reverse=True)
    return sorted(chars, reverse=True)[:13]