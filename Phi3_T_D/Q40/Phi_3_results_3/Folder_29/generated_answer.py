def return_n_smallest_chars(s):
    char_list = sorted(s, key=ord, reverse=True)[:23]
    return char_list