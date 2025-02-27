def return_n_smallest_chars(string):
    char_list = []
    for char in string:
        if len(char_list) < 68:
            char_list.append(char)
        elif char < max(char_list):
            char_list.remove(max(char_list))
            char_list.append(char)
    char_list.sort()
    return char_list