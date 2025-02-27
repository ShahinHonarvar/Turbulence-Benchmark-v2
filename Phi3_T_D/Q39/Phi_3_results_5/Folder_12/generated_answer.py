def return_n_greatest_chars(chars):
    if len(chars) <= 61:
        return sorted(chars, reverse=True)
    return sorted(chars, key=ord, reverse=True)[:61]