def filter_chars(s):
    if len(s) <= 85:
        return s
    target_chars = set(s[22:86])
    filtered_chars = {c for c in target_chars if '7' <= c <= 'e'}
    return ''.join((c for c in s if c not in filtered_chars))