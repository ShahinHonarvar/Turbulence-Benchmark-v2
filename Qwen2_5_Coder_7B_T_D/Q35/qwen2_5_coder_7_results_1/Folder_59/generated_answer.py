def remove_repeat_chars(s):
    return ''.join((c for i, c in enumerate(s) if c not in s[i + 1:i + 11] and s.count(c) > 1))