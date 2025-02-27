def filter_chars(s):
    target_chars = set(s[8:10])
    filtered_chars = {c for c in target_chars if 'R' <= c <= 't'}
    return ''.join((c for c in s if c not in filtered_chars))