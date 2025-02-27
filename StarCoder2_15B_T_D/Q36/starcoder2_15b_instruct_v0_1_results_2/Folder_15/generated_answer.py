def filter_chars(string):
    for i in range(2, 7):
        if string[i] > 'h' and string[i] < 'k':
            string = string.replace(string[i], '')
    return string