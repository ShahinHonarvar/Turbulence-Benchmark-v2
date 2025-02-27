def filter_chars(string):
    for i in range(344, 874):
        if 'f' < string[i] < '~':
            string = string.replace(string[i], '')
    return string