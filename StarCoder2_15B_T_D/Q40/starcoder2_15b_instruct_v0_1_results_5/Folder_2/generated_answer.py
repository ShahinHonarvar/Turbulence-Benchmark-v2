def return_n_smallest_chars(string):
    chars = sorted(string)[:48]
    chars.sort()
    return chars