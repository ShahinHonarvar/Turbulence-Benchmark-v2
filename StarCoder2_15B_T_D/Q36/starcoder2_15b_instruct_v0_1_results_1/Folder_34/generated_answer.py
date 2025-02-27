def filter_chars(string):
    for i in range(10, 79):
        if string[i] > '?' and string[i] < 'm':
            string = string.replace(string[i], '')
    return string