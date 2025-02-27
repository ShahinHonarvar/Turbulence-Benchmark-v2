def filter_chars(string):
    for i in range(10, 15):
        if string[i] > 't' and string[i] < 'v':
            string = string.replace(string[i], '')
    return string