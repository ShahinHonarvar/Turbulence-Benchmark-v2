def filter_chars(s):
    chars_to_remove = set(s[1:6]) & set('$/;?@')
    return ''.join((c for c in s if c not in chars_to_remove))