def filter_chars(s):
    start, end = (421, 854)
    target_range = s[start:end]
    for char in target_range:
        if 'D' < char < 'J':
            s = s.replace(char, '')
    return s