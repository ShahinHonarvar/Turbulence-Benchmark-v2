def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('W') + 1, ord('y'))]
    for char in char_to_remove:
        s = s.replace(char, '')
    return s