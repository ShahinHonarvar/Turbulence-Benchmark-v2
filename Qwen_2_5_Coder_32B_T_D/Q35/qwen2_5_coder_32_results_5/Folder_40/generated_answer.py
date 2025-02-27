def remove_repeat_chars(s):
    t = s[1:4]
    for c in set([x for x in t if t.count(x) > 1]):
        s = s.replace(c, '')
    return s