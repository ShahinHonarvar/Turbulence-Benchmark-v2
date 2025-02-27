def filter_chars(string):
    for i in range(69, 87):
        if chr(i) > '#' and chr(i) < 'L':
            string = string.replace(chr(i), '')
    return string