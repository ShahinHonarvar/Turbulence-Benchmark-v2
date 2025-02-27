def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('t') + 1, ord('v'))]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s