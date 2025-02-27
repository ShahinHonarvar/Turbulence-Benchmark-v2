def filter_chars(s):
    target_range = s[35:39]
    for char in target_range:
        if 'H' <= char <= 'e':
            s = s.replace(char, '')
    return s