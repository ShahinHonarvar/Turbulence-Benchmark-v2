def filter_chars(string):
    for i in range(56, 86):
        if string[i] > '+' and string[i] < 'w':
            string = string.replace(string[i], '')
    return string