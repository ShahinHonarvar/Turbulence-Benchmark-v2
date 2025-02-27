def filter_chars(s):
    chars_to_remove = set(s[24:80]) & set('abcdef')
    return ''.join((c for c in s if c not in chars_to_remove))