def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)
    return list(sorted_chars)[:23]