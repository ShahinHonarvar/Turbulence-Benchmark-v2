def filter_chars(s):
    char_to_remove = ''
    if len(s) > 2:
        char_to_remove = s[27]
        for char in s[27:30]:
            if ';' <= char <= 'b':
                char_to_remove += char
    return s.replace(char_to_remove, '')