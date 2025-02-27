def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('-') + 1, ord('L'))]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s