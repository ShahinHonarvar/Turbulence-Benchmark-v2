def filter_chars(s):
    target_chars = set(s[770:971])
    filtered_chars = {c for c in target_chars if '-' <= c <= 'D'}
    return ''.join((c for c in s if c not in filtered_chars))