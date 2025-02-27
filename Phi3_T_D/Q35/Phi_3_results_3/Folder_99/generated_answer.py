def remove_repeat_chars(s):
    target_range = set(s[450:905])
    return ''.join([c for i, c in enumerate(s) if c not in target_range or target_range.pop()])