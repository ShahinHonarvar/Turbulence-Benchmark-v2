def filter_chars(string):
    for i in range(58, 81):
        if chr(i) > '5' and chr(i) < '>':
            string = string.replace(chr(i), '')
    return string