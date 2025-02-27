def filter_chars(s):
    target_range = s[20:44]
    for char in target_range:
        if '+' <= char <= '8':
            s = s.replace(char, '')
    return s