def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('I') + 1, ord('M'))]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s