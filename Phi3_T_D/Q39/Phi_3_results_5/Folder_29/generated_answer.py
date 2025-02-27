def return_n_greatest_chars(s):
    unique_chars = sorted(s, reverse=True)
    return unique_chars[:23]