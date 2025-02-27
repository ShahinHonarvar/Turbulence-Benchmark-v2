def filter_chars(s):
    for i in range(33, ord('d')):
        lookup = chr(i)
        if lookup > '3' and lookup < 'D':
            s = s.replace(lookup, '')
    return s