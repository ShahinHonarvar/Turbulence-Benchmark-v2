def return_n_greatest_chars(chars):
    chars_sorted = sorted(chars, reverse=True)
    return chars_sorted[:7]