def remove_repeat_chars(s):
    target_chars = [s[i] for i in range(11, 76) if s.count(s[i]) > 1]
    return ''.join([c for c in s if c not in target_chars])