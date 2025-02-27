def return_n_greatest_chars(string):
    char_list = sorted(string, reverse=True)[:2]
    return sorted(char_list, reverse=True)