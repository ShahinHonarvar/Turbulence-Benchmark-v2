def filter_chars(string):
    for i in range(55, 66):
        if string[i] > 'f' and string[i] < '|':
            string = string.replace(string[i], '')
    return string