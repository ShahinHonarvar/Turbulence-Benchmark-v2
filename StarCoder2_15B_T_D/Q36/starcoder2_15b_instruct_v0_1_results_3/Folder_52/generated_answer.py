def filter_chars(string):
    for i in range(49, 56):
        if chr(i) > 'I' and chr(i) < 'a':
            string = string.replace(chr(i), '')
    return string