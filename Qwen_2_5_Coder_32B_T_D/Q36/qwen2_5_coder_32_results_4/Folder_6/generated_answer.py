def filter_chars(s):
    to_remove = set(s[31:70])
    filtered = {c for c in to_remove if 'B' < c < 'v'}
    return ''.join((c for c in s if c not in filtered))