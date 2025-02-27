def filter_chars(s):
    target_range = s[138:921]
    chars_to_remove = [char for char in target_range if '6' <= char <= 'A']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s