def return_n_smallest_chars(s):
    smallest_chars = sorted(list(s))[:52]
    smallest_chars.sort(reverse=True)
    return smallest_chars