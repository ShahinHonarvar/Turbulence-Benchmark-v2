def return_n_smallest_chars(s):
    smallest_char_ascii = sorted(s)[:29]
    smallest_char_ascii.reverse()
    return smallest_char_ascii