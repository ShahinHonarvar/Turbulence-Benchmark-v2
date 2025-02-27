def return_n_greatest_chars(str):
    char_list = list(str)
    char_list.sort(key=lambda x: ord(x), reverse=True)
    return sorted(char_list[:66])