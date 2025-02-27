def return_n_smallest_chars(text):
    chars = list(text)
    chars.sort()
    return chars[:80]