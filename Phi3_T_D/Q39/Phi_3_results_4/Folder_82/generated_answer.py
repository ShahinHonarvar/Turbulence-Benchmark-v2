def return_n_greatest_chars(s):
    char_list = sorted(s, reverse=True)
    return char_list[:60]