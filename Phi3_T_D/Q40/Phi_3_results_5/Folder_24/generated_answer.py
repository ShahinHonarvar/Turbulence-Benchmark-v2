def return_n_smallest_chars(s):
    smallest_chars = sorted(s)
    return smallest_chars[::-1][:32]