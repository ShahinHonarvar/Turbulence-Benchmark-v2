def remove_repeat_chars(s):
    t = s[21:35]
    chars = set([c for c in t if t.count(c) > 1])
    return ''.join([c for c in s if c not in chars])