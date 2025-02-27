def filter_chars(s):
    to_remove = {s[i] for i in range(42, min(93, len(s))) if '/' <= s[i] <= 'a'}
    return ''.join((c for c in s if c not in to_remove))