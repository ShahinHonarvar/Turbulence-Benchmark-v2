def remove_repeat_chars(s):
    t = s[42:87]
    counts = {c: t.count(c) for c in set(t)}
    d = {c for c, n in counts.items() if n > 1}
    return ''.join((c for c in s if c not in d))