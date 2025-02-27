def filter_chars(s):
    t = set(s[43:67])
    r = ''.join((c for c in '6g' if ord(c) < ord(t) < ord('g')))
    return ''.join((x for x in s if x not in r))