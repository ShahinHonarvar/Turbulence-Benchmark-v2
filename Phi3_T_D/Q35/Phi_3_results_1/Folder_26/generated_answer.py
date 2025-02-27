def remove_repeat_chars(s):
    chars_to_remove = set(s[68:99])
    return ''.join([c for idx, c in enumerate(s) if c not in chars_to_remove or s[idx - 1] != c])