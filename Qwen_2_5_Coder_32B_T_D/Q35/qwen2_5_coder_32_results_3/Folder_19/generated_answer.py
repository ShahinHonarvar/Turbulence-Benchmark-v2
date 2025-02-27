def remove_repeat_chars(s):
    t = s[2:4]
    for char in set([c for c in t if t.count(c) > 1]):
        s = s.replace(char, '')
    return s