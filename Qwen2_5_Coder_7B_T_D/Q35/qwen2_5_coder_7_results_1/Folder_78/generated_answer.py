def remove_repeat_chars(s):
    return ''.join([c for i, c in enumerate(s) if c not in s[62:97] or i < 62 or i >= 97])