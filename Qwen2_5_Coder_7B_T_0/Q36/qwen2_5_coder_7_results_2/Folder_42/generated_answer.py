def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('t') + 1, ord('x'))]
    for char in target_chars:
        s = s.replace(char, '')
    return s