def filter_chars(s):
    target_chars = set(s[12:89] if len(s) > 88 else s[12:])
    target_chars = {c for c in target_chars if '&' <= c <= 'v'}
    return ''.join((c for c in s if c not in target_chars))