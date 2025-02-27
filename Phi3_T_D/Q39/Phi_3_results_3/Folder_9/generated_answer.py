def return_n_greatest_chars(chars):
    greatest_chars = sorted(chars, reverse=True)[:20]
    greatest_chars.sort()
    return greatest_chars