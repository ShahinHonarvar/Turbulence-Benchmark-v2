def filter_chars(s):
    for i in range(82, 92):
        if '!' < s[i] < '*':
            s = s.replace(s[i], '')
    return s