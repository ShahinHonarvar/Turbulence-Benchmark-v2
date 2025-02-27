def remove_repeat_chars(s):
    t = s[38:52]
    d = {c for c in t if t.count(c) > 1}
    return ''.join((c for c in s if c not in d))