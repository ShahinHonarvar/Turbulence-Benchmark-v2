def return_n_smallest_chars(s):
    char_list = list(s)
    char_list.sort(key=ord)
    return char_list[:45]