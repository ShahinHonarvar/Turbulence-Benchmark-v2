def filter_chars(string):
    char_list = list(string)
    for i in range(46, 74):
        if char_list[i] > '&' and char_list[i] < 'M':
            char_list[i] = ''
    return ''.join(char_list)