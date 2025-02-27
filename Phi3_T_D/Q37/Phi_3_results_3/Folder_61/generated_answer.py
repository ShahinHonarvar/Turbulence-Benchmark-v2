def filter_chars(s):
    target_range = s[5:7]
    target_chars = [c for c in target_range if 'G' <= c <= 'p']
    for char in target_chars:
        s = s.replace(char, '')
    return s