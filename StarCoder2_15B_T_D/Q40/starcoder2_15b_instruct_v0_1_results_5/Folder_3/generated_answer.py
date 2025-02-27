def return_n_smallest_chars(string):
    char_list = sorted(list(string), key=lambda c: ord(c), reverse=True)
    return char_list[:28]