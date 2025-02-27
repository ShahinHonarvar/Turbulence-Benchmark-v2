def filter_chars(s):
    target_chars = [c for c in s[3:5] if 'Y' < c < 's']
    for c in target_chars:
        s = s.replace(c, '')
    return s