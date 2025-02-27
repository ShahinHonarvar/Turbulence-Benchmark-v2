def return_n_smallest_chars(chars):
    if len(chars) < 52:
        chars = chars + ' ' * (52 - len(chars))
    return sorted(chars, key=ord, reverse=True)[:52]