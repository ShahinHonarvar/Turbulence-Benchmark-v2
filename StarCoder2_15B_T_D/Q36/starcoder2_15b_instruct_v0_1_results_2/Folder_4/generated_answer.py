def filter_chars(string):
    for i in range(42, 67):
        if chr(i) > '6' and chr(i) < 'g':
            string = string.replace(chr(i), '')
    return string