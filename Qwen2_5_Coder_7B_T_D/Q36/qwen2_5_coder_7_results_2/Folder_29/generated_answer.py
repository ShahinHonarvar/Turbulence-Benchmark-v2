def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('H') + 1, ord('s'))]
    for char in char_to_remove:
        s = s.replace(char, '')
    return s[46:68]