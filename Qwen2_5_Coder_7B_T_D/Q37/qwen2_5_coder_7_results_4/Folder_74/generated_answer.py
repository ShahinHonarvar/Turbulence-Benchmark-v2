def filter_chars(s):
    to_remove = [c for c in s[19:33] if 'f' <= c <= 'o']
    remove_set = set(to_remove)
    return ''.join((c for c in s if c not in remove_set))