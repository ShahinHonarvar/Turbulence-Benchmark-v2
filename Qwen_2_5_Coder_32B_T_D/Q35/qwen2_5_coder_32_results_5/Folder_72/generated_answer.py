def remove_repeat_chars(s):
    if len(s) <= 70:
        return s
    sub = s[13:70]
    rep_chars = {c for c in sub if sub.count(c) > 1}
    return ''.join((c for c in s if c not in rep_chars))