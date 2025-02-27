def remove_repeat_chars(s):
    t = s[1:10]
    counts = {c: t.count(c) for c in t}
    return ''.join((c for c in s if counts.get(c, 0) == 1 or c not in counts))