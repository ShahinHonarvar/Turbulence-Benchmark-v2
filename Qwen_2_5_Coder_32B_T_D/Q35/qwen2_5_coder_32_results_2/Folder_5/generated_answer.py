def remove_repeat_chars(s):
    t = s[2:8]
    for char in set([c for c in t if t.count(c) > 1]):
        s = ''.join((c for c in s if c != char))
    return s