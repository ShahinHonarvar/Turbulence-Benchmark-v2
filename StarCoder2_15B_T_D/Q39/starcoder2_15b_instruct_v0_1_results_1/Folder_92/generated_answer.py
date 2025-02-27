def return_n_greatest_chars(str):
    char_list = list(str)
    char_list.sort(key=lambda c: ord(c), reverse=True)
    return sorted(char_list[:63])