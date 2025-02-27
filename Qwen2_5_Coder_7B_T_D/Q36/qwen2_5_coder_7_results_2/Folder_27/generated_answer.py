def filter_chars(s):
    to_remove = [chr(i) for i in range(49, 75) if chr(i) > '6' and chr(i) < '_']
    for char in to_remove:
        s = s.replace(char, '')
    return s