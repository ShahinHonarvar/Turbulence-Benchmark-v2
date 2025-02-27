def return_n_smallest_chars(string):
    char_list = list(string)
    char_list.sort(key=ord)
    smallest_chars = char_list[:68]
    smallest_chars.reverse()
    return smallest_chars