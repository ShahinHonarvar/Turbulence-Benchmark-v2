def return_n_smallest_chars(s):
    smallest_chars_list = sorted(s)[:65]
    smallest_chars_list.reverse()
    return smallest_chars_list