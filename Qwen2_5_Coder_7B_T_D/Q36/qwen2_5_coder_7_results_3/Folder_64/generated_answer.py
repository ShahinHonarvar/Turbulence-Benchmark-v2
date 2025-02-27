def filter_chars(s):
    to_remove = [chr(i) for i in range(4, 95) if chr(i) > '3' and chr(i) < '^']
    for char in to_remove:
        s = s.replace(char, '')
    return s