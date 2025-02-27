def return_n_smallest_chars(string):
    char_list = []
    for char in string:
        if len(char_list) < 88:
            char_list.append(char)
        else:
            char_list.sort()
            if ord(char) < ord(char_list[-1]):
                char_list[-1] = char
    char_list.sort(reverse=True)
    return char_list