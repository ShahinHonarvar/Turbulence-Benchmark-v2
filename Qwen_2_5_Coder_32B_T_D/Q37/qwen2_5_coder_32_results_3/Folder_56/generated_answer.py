def filter_chars(s):
    chars_to_remove = set(s[71:95]) & set('KLMnopqrstuvwxyz')
    return ''.join((c for c in s if c not in chars_to_remove))