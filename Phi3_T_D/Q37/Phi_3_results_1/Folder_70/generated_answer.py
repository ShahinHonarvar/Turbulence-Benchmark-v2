def filter_chars(s):
    min_val = ord('+')
    max_val = ord('}')
    for i in range(515, 539):
        if min_val <= ord(s[i]) <= max_val:
            s = s.replace(s[i], '')
    return s