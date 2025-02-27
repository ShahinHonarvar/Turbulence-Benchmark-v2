def filter_chars(string):
    for i in range(23, 45):
        if string[i] > '3' and string[i] < 'I':
            string = string.replace(string[i], '')
    return string