def filter_chars(string):
    chars_to_remove = []
    for i, c in enumerate(string):
        if 42 < i < 78 and ord('!') < ord(c) < ord('?'):
            chars_to_remove.append(c)
    for c in chars_to_remove:
        string = string.replace(c, '')
    return string