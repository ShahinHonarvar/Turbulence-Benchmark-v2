def return_n_greatest_chars(string):
    char_list = list(string)
    sorted_list = sorted(char_list, key=lambda x: ord(x), reverse=True)
    return sorted_list[:35]