def return_n_smallest_chars(string):
    char_list = sorted(list(string), key=ord)
    return char_list[:35][::-1]