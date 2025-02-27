def return_n_greatest_chars(chars):
    if len(chars) > 46:
        chars = chars[:46]
    sorted_chars = sorted(chars, key=lambda c: -ord(c))
    return sorted_chars[:46]