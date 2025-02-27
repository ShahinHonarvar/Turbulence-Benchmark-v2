def filter_chars(s):
    if len(s) <= 403:
        chars_to_remove = set(s[155:404]) & set('[]^_`abcd')
    else:
        chars_to_remove = set(s[155:404]) & set('[]^_`abcdefghijklmnopqrstuvwxyz{|}')
    return ''.join((c for c in s if c not in chars_to_remove))