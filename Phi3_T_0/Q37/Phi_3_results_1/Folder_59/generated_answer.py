def filter_chars(s):
    char_to_remove = s[2:4]
    for char in char_to_remove:
        if '5' <= char <= '_':
            s = s.replace(char, '')
    return s