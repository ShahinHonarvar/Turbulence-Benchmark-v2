def filter_chars(s):
    if len(s) < 404:
        return s
    chars_to_remove = set(s[155:404]) & set('[]^_`{|}')
    return ''.join((c for c in s if c not in chars_to_remove))