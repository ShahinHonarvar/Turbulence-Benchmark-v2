def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)
    greatest_chars = sorted_chars[:29]
    greatest_chars.sort()
    return greatest_chars