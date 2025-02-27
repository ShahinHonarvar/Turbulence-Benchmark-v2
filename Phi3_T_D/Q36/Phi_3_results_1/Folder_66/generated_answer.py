def filter_chars(s):
    for i in range(39, 87):
        if '!' < s[i] < '}':
            s = s.replace(s[i], '')
    return s