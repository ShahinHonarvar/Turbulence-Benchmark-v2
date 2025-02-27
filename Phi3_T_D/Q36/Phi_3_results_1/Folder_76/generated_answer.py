def filter_chars(s):
    chars_to_remove = [c for c in s[669:888] if 'B' < c < 'Y']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s