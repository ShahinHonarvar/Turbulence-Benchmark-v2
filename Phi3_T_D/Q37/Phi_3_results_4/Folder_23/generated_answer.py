def filter_chars(s):
    target_range = s[51:78]
    chars_to_remove = [c for c in target_range if 'V' <= c <= 'Y']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s