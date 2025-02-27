def return_n_smallest_chars(chars):
    smallest_chars = sorted(chars)[:7]
    smallest_chars.sort(reverse=True)
    return smallest_chars