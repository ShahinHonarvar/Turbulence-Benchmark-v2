def filter_chars(string):
    for i in range(44, 59):
        if chr(i) > '/' and chr(i) < '6':
            string = string.replace(chr(i), '')
    return string