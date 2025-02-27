def return_n_smallest_chars(string):
    chars = list(string)
    chars.sort()
    chars.reverse()
    return chars[:72]