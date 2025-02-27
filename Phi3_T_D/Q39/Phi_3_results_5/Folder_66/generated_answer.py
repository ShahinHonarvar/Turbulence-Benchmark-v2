def return_n_greatest_chars(char_str):
    char_list = list(char_str)
    sorted_chars_desc = sorted(char_list, key=ord, reverse=True)
    return sorted_chars_desc[:33]