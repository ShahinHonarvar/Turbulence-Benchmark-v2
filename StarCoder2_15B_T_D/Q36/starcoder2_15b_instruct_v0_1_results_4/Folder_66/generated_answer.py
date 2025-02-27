def filter_chars(string):
    for i in range(39, 87):
        if chr(i) > '!' and chr(i) < '}':
            string = string.replace(chr(i), '')
    return string