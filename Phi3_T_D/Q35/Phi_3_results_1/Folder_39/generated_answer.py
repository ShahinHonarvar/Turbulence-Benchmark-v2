def remove_repeat_chars(s):
    target_chars = []
    for i, c in enumerate(s[44:90]):
        if s[44:90].count(c) > 1 and c not in target_chars:
            target_chars.append(c)
    return ''.join((c for c in s if c not in target_chars or not 44 <= s.find(c) % 91 < 90))