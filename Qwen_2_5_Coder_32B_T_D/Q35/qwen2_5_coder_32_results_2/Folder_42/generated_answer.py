def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    sub = s[19:60]
    counts = {c: sub.count(c) for c in set(sub) if sub.count(c) > 1}
    result = [c for c in s if c not in counts]
    return ''.join(result)