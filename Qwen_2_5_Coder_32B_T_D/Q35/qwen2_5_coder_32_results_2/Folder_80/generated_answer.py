def remove_repeat_chars(s):
    if len(s) <= 84:
        return s
    part = s[57:84]
    counts = {c: part.count(c) for c in part if part.count(c) > 1}
    return ''.join((c for c in s if c not in counts))