def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)
    n_greatest_chars = sorted_chars[:52]
    return sorted(n_greatest_chars)