def filter_chars(s):
    to_remove = {c for c in s[78:81] if 'S' < c < '['}
    return ''.join((c for c in s if c not in to_remove))