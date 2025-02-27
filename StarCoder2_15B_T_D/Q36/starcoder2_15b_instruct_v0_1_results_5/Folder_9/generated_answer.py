def filter_chars(string):
    for i in range(50, 92):
        if string[i] > 'A' and string[i] < 'Q':
            string = string.replace(string[i], '')
    return string