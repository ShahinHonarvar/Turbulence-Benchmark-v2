def filter_chars(s):
    chars = [c for c in s[88:91] if 'J' <= c <= 'Q']
    for char in chars:
        s = s.replace(char, '')
    return s