def filter_chars(string):
    char_list = list(string)
    for i in range(31, 70):
        if char_list[i] > 'B' and char_list[i] < 'v':
            char_list.remove(char_list[i])
    return ''.join(char_list)