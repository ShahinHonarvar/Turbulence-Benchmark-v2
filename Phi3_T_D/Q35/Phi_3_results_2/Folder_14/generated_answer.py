def remove_repeat_chars(s):
    target_chars = {c for c in s[2:5] if s[2:5].count(c) > 1}
    return ''.join((c for c in s if c not in target_chars))