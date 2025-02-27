def filter_chars(s):
    if len(s) > 3:
        char = s[2:4:2]
        return s.replace(char, '')
    return s