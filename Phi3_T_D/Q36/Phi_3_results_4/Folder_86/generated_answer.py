def filter_chars(s):
    start, end = (672, 709)
    for i in range(start, end):
        if 'X' < s[i] < '}':
            s = s.replace(s[i], '')
    return s