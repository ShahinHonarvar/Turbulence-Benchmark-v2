def filter_chars(s):
    t = s[21:25]
    for c in t:
        if '5' < c < '}':
            s = ''.join([x for x in s if x != c])
    return s