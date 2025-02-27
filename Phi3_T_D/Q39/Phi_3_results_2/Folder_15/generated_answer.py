def return_n_greatest_chars(s):
    char_list = sorted(s, reverse=True)[:57]
    char_list.sort()
    return char_list