def remove_repeat_chars(s):
    if len(s) < 74:
        return s
    target_chars = set(s[20:93])
    return ''.join((c for i, c in enumerate(s) if (i < 20 or i >= 93) or c not in target_chars))