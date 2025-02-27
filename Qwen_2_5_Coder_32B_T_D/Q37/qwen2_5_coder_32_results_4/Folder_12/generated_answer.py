def filter_chars(s):
    chars_to_remove = set(s[19:91]) & set('FGHIgh')
    return ''.join((c for c in s if c not in chars_to_remove))