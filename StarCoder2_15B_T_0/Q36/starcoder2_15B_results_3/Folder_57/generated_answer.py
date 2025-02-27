def filter_chars(string):
    for i in range(70, 74):
        if chr(i) > 'A' and chr(i) < 'U':
            string = string.replace(chr(i), '')
    return string