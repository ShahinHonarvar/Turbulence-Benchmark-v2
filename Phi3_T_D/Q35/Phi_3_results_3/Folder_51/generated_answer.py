def remove_repeat_chars(s):
    repeat_chars = set([s[i] for i in range(6, 9) if s.count(s[i], 6, 9) > 1])
    return ''.join((c for c in s if c not in repeat_chars))