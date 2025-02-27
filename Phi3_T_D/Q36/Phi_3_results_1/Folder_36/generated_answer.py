def filter_chars(s):
    target_range = s[283:484]
    characters_to_remove = [c for c in target_range if 'l' < c < 't']
    for char in characters_to_remove:
        s = s.replace(char, '')
    return s