def filter_chars(s):
    to_remove = {c for c in s[3:8] if '?' < c < 'k'}
    return ''.join((c for c in s if c not in to_remove))