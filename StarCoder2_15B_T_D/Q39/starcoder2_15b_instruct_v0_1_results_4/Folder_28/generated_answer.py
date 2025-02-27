def return_n_greatest_chars(string):
    char_list = list(string)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return sorted(char_list[:3])