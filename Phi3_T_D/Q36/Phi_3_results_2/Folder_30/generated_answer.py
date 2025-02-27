def filter_chars(s):
    char_range = '456789:;<=>[\\]^_`{|}~'
    for i in range(23, 45):
        if s[i] in char_range:
            s = s.replace(s[i], '')
    return s