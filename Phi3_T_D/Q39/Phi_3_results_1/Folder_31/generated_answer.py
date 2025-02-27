def return_n_greatest_chars(chars):
    unique_chars = sorted(set(chars), reverse=True)
    return unique_chars[:70]