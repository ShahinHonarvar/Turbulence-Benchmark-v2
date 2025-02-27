def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('S') + 1, ord('m'))]
    for char in char_to_remove:
        s = s.replace(char, '')
    return s