def remove_repeat_chars(s):
    t = s[56:90]
    repeat_chars = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))