def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    sub = s[91:200]
    counts = {c: sub.count(c) for c in sub if sub.count(c) > 1}
    return ''.join((c for c in s if c not in counts))