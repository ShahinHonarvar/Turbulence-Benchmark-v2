def filter_chars(string):
    for i in range(82, 89):
        if chr(i) > '*' and chr(i) < '[':
            string = string.replace(chr(i), '')
    return string