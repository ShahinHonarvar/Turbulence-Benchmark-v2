def remove_repeat_chars(s):
    if len(s) <= 926:
        return s
    sub = s[376:926]
    chars = {c for c in sub if sub.count(c) > 1}
    return ''.join((c for c in s if c not in chars))