def filter_chars(string):
    for i in range(55, 66):
        if chr(i) > 'f' and chr(i) < '|':
            string = string.replace(chr(i), '')
    return string