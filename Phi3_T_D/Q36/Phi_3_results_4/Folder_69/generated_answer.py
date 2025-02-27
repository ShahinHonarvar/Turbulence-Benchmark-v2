def filter_chars(s):
    for index in range(343, 665):
        char_to_remove = s[index]
        if '%' < char_to_remove < 'U':
            s = s.replace(char_to_remove, '')
    return s