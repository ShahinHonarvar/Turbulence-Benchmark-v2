def filter_chars(s):
    for i in range(1, 9):
        char = chr(ord('A') + i)
        s = s.replace(char, '')
    return s