def remove_repeat_chars(s):
    if len(s) <= 97:
        return s
    t = s[27:96]
    repeat_chars = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))