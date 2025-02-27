def remove_repeat_chars(s):
    if len(s) <= 43:
        return s
    sub = s[38:43]
    counts = {c: sub.count(c) for c in sub}
    to_remove = {c for c, cnt in counts.items() if cnt > 1}
    return ''.join((c for c in s if c not in to_remove))