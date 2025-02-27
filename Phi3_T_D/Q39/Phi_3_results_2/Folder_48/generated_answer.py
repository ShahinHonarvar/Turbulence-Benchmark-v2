def return_n_greatest_chars(chars):
    greatest_chars = sorted(chars, reverse=True)[:12]
    return sorted(greatest_chars)