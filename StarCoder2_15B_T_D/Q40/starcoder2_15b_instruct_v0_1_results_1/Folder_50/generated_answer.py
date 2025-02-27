def return_n_smallest_chars(string):
    char_list = list(string)
    char_list.sort(key=lambda x: ord(x))
    return char_list[:16][::-1]