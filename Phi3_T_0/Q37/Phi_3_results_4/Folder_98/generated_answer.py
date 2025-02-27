def filter_chars(s):
    char_to_remove = s[8:10]
    for char in char_to_remove:
        s = s.replace(char, '')
    return s