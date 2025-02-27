def filter_chars(s):
    if len(s) < 921:
        return s
    target_chars = set(s[138:921])
    filtered_chars = {c for c in target_chars if '6' <= c <= 'A'}
    return ''.join((c for c in s if c not in filtered_chars))