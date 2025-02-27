def remove_repeat_chars(s):
    t = s[1:7]
    counts = {c: t.count(c) for c in set(t) if t.count(c) > 1}
    return ''.join((c for c in s if c not in counts))