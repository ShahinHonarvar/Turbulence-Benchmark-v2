def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    t = s[40:200]
    r = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in r))