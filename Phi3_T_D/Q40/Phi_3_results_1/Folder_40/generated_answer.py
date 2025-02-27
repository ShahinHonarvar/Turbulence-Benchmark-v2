def return_n_smallest_chars(s):
    char_list = sorted(s)
    return list(reversed(char_list[:7]))