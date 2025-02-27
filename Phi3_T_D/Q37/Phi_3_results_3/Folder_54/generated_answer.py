def filter_chars(string):
    for i in range(46, 86):
        char = string[i]
        if '-' <= char <= 'X':
            string = string.replace(char, '', 1)
    return string