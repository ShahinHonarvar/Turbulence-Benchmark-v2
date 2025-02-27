def remove_repeat_chars(s):
    start, end = (45, 48)
    target_chars = set(s[start + 1:end])
    return ''.join((c for i, c in enumerate(s) if i < start or c not in target_chars or i >= end or (c in target_chars)))