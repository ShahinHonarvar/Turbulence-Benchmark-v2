def return_n_greatest_chars(chars):
    if len(chars) < 24:
        return chars
    return sorted(chars, key=ord, reverse=True)[:24]