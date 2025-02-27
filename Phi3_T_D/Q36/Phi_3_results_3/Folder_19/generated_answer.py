def filter_chars(s):
    target_chars = [c for c in s[77:87] if ';' < c < 'r']
    for char in target_chars:
        s = s.replace(char, '')
    return s