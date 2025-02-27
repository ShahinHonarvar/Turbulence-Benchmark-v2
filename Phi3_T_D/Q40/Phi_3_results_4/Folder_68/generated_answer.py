def return_n_smallest_chars(s):
    n = 89
    chars = sorted(s, reverse=True)[:n]
    chars.sort(reverse=True)
    return chars