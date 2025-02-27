def return_n_greatest_chars(s):
    char_list = sorted(list(s), reverse=True)
    return char_list[:40]