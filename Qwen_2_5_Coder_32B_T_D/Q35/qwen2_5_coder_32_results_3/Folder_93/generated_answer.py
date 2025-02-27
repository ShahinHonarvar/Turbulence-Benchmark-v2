def remove_repeat_chars(s):
    t = s[57:85]
    repeats = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in repeats))