def filter_chars(string):
    for i in range(154, 222):
        if string[i] > 'A' and string[i] < 'f':
            string = string.replace(string[i], '')
    return string