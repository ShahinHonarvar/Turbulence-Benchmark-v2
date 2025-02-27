def filter_chars(string):
    for i in range(170, 195):
        if chr(i) > '!' and chr(i) < '}':
            string = string.replace(chr(i), '')
    return string