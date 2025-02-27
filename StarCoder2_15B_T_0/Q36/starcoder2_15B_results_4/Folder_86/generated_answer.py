def filter_chars(string):
    for i in range(672, 709):
        if chr(i) > 'X' and chr(i) < '}':
            string = string.replace(chr(i), '')
    return string