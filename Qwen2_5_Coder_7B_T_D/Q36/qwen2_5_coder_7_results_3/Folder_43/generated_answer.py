def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('A') + 1, ord('i'))]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s