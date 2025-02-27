def remove_repeat_chars(s):
    unique_chars = set(s[42:87])
    return ''.join((c for i, c in enumerate(s[42:87]) if c not in unique_chars or (c in unique_chars and list(s[42:87]).count(c) == 1))) + s[87:]