def filter_chars(s):
    for char in range(ord('m'), ord('w') + 1):
        s = s.replace(chr(char), '')
    return s