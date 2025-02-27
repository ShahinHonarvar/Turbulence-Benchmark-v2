def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    t = s[17:87]
    repeat_chars = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in repeat_chars))