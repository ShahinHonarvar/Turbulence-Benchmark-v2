def filter_chars(s):
    for i in range(57, 69):
        char_to_remove = s[i]
        if ord('(') < ord(char_to_remove) < ord('W'):
            s = s.replace(char_to_remove, '')
    return s