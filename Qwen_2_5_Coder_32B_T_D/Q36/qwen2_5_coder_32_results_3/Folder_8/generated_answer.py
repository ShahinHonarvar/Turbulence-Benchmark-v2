def filter_chars(s):
    to_remove = set(s[82:93])
    filtered = {c for c in to_remove if '!' < c < '*'}
    return ''.join((c for c in s if c not in filtered))