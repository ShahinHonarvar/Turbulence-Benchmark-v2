def return_n_smallest_chars(string):
    char_list = sorted(string)[:64]
    char_list.sort()
    return char_list