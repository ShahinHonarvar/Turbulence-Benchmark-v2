def filter_chars(s):
    target_range = s[19:23]
    target_chars = [c for c in target_range if ord(']') <= ord(c) <= ord('t')]
    for char in target_chars:
        s = s.replace(char, '')
    return s