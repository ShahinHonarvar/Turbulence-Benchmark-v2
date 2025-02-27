def filter_chars(s):
    char_to_filter = s[73:75]
    for ch in set(char_to_filter):
        if 'U' <= ch <= 'l':
            s = s.replace(ch, '')
    return s