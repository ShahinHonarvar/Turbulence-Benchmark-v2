def return_n_greatest_chars(s):
    char_list = list(s)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return char_list[:19]