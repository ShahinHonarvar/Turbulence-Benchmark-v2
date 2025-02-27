def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    sub = s[21:35]
    char_count = {c: sub.count(c) for c in set(sub) if sub.count(c) > 1}
    return ''.join((c for c in s if c not in char_count))