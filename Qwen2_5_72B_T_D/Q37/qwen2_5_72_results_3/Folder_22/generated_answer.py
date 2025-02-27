def filter_chars(s):
    remove_chars = set([c for c in s[33:71] if '7' <= c <= 'k'])
    return ''.join([c for c in s if c not in remove_chars])