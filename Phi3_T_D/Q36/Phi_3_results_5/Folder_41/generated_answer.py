def filter_chars(s):
    for i in range(81, 89):
        char_to_remove = s[i]
        if 'f' < char_to_remove < '{':
            s = s.replace(char_to_remove, '')
    return s