def return_n_smallest_chars(s):
    char_list = sorted(s)
    if len(char_list) > 87:
        return char_list[:87]
    else:
        return char_list