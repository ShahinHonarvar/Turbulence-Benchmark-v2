def filter_chars(s):
    target_range = s[477:985]
    target_chars = {char for char in target_range if ',' <= char <= 'V'}
    for char in target_chars:
        s = s.replace(char, '')
    return s