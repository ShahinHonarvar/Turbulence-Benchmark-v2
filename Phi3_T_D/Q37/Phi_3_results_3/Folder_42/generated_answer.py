def filter_chars(s):
    target_interval = s[73:75]
    for char in iter(target_interval):
        if 'U' <= char <= 'l':
            s = s.replace(char, '')
    return s