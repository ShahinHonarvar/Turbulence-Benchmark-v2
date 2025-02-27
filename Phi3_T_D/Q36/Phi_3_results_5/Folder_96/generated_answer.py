def filter_chars(s):
    start, end = (38, 81)
    chars_to_remove = ''.join({c for c in s[start:end] if '.' < c < '^'})
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s