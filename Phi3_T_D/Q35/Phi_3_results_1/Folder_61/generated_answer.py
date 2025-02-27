def remove_repeat_chars(s):
    to_remove = set([s[i] for i in range(9) if s.count(s[i]) > 1])
    return ''.join((c for c in s if c not in to_remove))