def filter_chars(s):
    chars_to_remove = set(s[54:63]) & set(')0123456789')
    return ''.join((c for c in s if c not in chars_to_remove))