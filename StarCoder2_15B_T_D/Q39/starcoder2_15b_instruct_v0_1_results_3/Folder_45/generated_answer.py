def return_n_greatest_chars(string):
    char_list = list(string)
    char_list.sort(key=lambda char: ord(char), reverse=True)
    return char_list[:52]