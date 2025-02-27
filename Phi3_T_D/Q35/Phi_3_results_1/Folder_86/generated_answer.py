def remove_repeat_chars(s):
    if len(s) < 32:
        return s
    repeat_chars = set([s[i] for i in range(19, 32) if s.count(s[i]) > 1])
    return ''.join((c for c in s if c not in repeat_chars))