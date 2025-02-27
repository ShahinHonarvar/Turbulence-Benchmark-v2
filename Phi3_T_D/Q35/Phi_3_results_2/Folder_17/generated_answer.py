def remove_repeat_chars(s):
    start, end = (73, 84)
    target_chars = {c for c in s[start:end] if s[start:end].count(c) > 1}
    return ''.join((c for i, c in enumerate(s) if c not in target_chars or not (start <= i < end and c in target_chars)))