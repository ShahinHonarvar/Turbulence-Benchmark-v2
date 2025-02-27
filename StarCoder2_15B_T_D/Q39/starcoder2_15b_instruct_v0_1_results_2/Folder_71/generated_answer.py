def return_n_greatest_chars(string):
    char_list = list(string)
    sorted_char_list = sorted(char_list, key=lambda char: ord(char), reverse=True)
    return sorted_char_list[:14]