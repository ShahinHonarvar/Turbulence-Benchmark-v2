def remove_repeat_chars(s):
    target_chars = set(s[38:52])
    return ''.join((c for i, c in enumerate(s) if c not in target_chars or s[38:52].count(c) == 1))