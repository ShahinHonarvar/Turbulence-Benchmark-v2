def filter_chars(s):
    char_to_remove = s[73:74 + 1]
    for char in char_to_remove:
        if 'U' <= char <= 'l':
            s = s.replace(char, '')
    return s