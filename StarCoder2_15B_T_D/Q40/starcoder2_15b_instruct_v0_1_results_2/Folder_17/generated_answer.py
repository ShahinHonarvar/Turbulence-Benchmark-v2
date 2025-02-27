def return_n_smallest_chars(string):
    char_list = list(string)
    char_list.sort(key=lambda c: ord(c))
    return char_list[:11]