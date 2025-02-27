def filter_chars(s):
    if len(s) < 5:
        return s
    target_char = s[4]
    if '7' <= target_char <= 'o':
        return s.replace(target_char, '')
    return s