def return_n_greatest_chars(chars):
    if len(chars) < 32:
        return sorted(chars, key=ord)
    else:
        return sorted(chars, key=ord, reverse=True)[:32]