def filter_chars(s):
    to_remove = ''.join([chr(i) for i in range(32, 51) if chr(i) > '/' and chr(i) < 'J'])
    for char in to_remove:
        s = s.replace(char, '')
    return s