def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('A') + 1, ord('U'))]
    for char in char_to_remove:
        s = s.replace(char, '')
    return s