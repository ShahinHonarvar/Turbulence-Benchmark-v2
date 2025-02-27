def return_n_smallest_chars(string):
    char_list = []
    for char in string:
        char_list.append(char)
    char_list.sort(key=ord)
    return char_list[-32:]