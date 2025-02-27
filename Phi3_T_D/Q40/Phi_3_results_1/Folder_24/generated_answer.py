def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort(key=ord, reverse=True)
    return chars[:32]