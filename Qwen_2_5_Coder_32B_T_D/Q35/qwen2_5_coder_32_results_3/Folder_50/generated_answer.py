def remove_repeat_chars(s):
    if len(s) <= 77:
        return s
    t = s[14:76]
    repeats = {c for c in t if t.count(c) > 1}
    return s[0:14] + ''.join((c for c in s[14:] if c not in repeats))