def filter_chars(string):
    for i in range(42, 68):
        if string[i] > 't' and string[i] < 'x':
            string = string.replace(string[i], '')
    return string