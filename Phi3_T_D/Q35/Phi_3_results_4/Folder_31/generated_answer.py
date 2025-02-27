def remove_repeat_chars(s):
    chars = set([c for c in s[33:78] if s[33:78].count(c) > 1])
    return ''.join([c for c in s if c not in chars or not 33 <= s.index(c) < 78])