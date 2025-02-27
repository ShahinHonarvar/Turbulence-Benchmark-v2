def filter_chars(s):
    target_range = s[379:901]
    chars_to_remove = [c for c in target_range if 'M' <= c <= 'v']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s