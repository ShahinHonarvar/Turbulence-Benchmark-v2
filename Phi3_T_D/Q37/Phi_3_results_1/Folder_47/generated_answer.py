def filter_chars(s):
    for i in range(38, 55):
        char_to_remove = s[i]
        if ':' <= char_to_remove <= 'r':
            s = s.replace(char_to_remove, '')
    return s