def remove_repeat_chars(s):
    unique_chars = set([s[i] for i in range(36, 85) if s.count(s[i]) > 1])
    return ''.join([c for i, c in enumerate(s) if c not in unique_chars or 36 <= i < 85] + [c for i, c in enumerate(s) if c in unique_chars and 36 <= i <= 85])