def return_n_smallest_chars(string):
    char_list = list(string)
    sorted_char_list = sorted(char_list)
    return sorted_char_list[-7:]