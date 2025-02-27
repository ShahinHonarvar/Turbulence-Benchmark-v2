def filter_chars(string):
    for i in range(722, 833):
        if chr(i) >= 'K' and chr(i) <= 'm':
            string = string.replace(chr(i), '')
    return string