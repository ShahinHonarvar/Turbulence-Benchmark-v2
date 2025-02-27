def remove_repeat_chars(s):
    chars_to_remove = set(s[7:9])
    return ''.join((c for i, c in enumerate(s) if c not in chars_to_remove or not s[7:9].count(c)))