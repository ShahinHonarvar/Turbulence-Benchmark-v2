def filter_chars(s):
    target_chars = set(s[24:80]) & set('abcdef')
    return ''.join((c for c in s if c not in target_chars))