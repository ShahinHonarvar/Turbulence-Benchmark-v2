def filter_chars(s):
    char_range = [c for c in s[18:31] if 'H' < c < '|']
    for c in char_range:
        s = s.replace(c, '')
    return s