def return_n_greatest_chars(chars):
    if len(chars) >= 38:
        greatest_chars = sorted(chars, reverse=True)[:38]
    else:
        greatest_chars = sorted(chars, reverse=True)
    return greatest_chars