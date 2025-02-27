def filter_chars(s):
    to_remove = set((chr(i) for i in range(34, 126) if chr(i) > '!' and chr(i) < '}'))
    for char in to_remove:
        s = s.replace(char, '')
    return s