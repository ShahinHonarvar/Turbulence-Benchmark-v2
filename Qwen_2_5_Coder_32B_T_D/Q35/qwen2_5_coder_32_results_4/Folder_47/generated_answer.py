def remove_repeat_chars(s):
    if len(s) <= 53:
        return s
    t = s[30:53]
    counts = {c: t.count(c) for c in set(t) if t.count(c) > 1}
    return ''.join((c for c in s if c not in counts))