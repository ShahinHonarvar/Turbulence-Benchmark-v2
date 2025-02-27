def return_n_greatest_chars(string):
    char_list = list(string)
    char_list.sort(key=lambda c: ord(c), reverse=True)
    return char_list[:11]