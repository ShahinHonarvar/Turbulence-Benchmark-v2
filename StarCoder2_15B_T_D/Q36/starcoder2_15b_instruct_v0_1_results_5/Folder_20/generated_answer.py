def filter_chars(string):
    for i in range(13, 40):
        if string[i] > ':' and string[i] < 'C':
            string = string.replace(string[i], '')
    return string