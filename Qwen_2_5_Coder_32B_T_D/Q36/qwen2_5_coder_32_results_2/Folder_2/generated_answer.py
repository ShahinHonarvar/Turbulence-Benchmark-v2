def filter_chars(s):
    if len(s) < 854:
        return s
    chars_to_remove = set(s[421:854])
    chars_to_remove = {c for c in chars_to_remove if 'D' < c < 'J'}
    return ''.join((c for c in s if c not in chars_to_remove))