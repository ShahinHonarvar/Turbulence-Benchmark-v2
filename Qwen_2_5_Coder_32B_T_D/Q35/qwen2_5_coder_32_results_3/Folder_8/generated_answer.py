def remove_repeat_chars(s):
    t = s[45:48]
    chars = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in chars))