def remove_repeat_chars(s):
    t = s[57:88]
    chars = {c for c in t if t.count(c) > 1}
    return ''.join([c for c in s if c not in chars])