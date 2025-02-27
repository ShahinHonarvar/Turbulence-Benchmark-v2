def filter_chars(s):
    excluded_char = None
    for i in range(502, 946):
        if 'W' < s[i] < 'y':
            excluded_char = s[i]
            break
    if excluded_char:
        return s.replace(excluded_char, '')
    return s