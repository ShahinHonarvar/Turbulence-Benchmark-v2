def filter_chars(s):
    for char in range(ord('W') + 1, ord('y')):
        s = s.replace(chr(char), '')
    return s