def filter_chars(s):
    to_remove = {s[i] for i in range(12, 26) if 'P' <= s[i] <= 'x'}
    return ''.join((c for c in s if c not in to_remove))