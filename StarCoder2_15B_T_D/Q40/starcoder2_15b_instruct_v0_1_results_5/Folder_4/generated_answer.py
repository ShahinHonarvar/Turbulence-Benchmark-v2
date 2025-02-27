def return_n_smallest_chars(s):
    chars = list(s)
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[-90:]