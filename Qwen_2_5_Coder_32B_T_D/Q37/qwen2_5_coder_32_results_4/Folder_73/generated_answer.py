def filter_chars(s):
    if len(s) < 86:
        return s
    target_chars = set(s[22:86])
    target_chars = {c for c in target_chars if '7' <= c <= 'e'}
    return ''.join((c for c in s if c not in target_chars))