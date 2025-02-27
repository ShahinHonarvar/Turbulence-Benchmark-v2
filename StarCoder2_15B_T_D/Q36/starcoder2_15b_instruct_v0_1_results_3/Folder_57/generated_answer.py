def filter_chars(string):
    for i in range(70, 74):
        if string[i] > 'A' and string[i] < 'U':
            string = string.replace(string[i], '')
    return string