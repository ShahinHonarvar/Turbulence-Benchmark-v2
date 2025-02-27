def filter_chars(s):
    chars_to_remove = set(s[19:23])
    filter_set = {c for c in chars_to_remove if ']' <= c <= 't'}
    return ''.join((c for c in s if c not in filter_set))