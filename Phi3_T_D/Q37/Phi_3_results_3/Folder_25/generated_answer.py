def filter_chars(s):
    sub = s[30:39]
    to_remove = [c for c in sub if ';' <= c <= 'g']
    for c in set(to_remove):
        s = s.replace(c, '')
    return s