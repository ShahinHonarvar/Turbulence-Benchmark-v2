def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('K') + 1, ord('a'))]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s