def remove_repeat_chars(s):
    chars = set(s[3:8])
    return ''.join((c for i, c in enumerate(s) if i < 3 or i >= 8 or c not in chars))