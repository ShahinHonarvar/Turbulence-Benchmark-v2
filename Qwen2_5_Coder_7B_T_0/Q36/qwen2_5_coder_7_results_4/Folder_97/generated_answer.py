def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('S') + 1, ord('m'))]
    for char in target_chars:
        s = s.replace(char, '')
    return s