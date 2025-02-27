def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)[:11]
    return sorted_chars