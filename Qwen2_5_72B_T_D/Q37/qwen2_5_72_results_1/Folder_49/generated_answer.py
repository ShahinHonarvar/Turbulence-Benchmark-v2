def filter_chars(s):
    to_remove = set([c for c in s[42:98] if '*' <= c <= 'b'])
    result = ''.join([c for c in s if c not in to_remove])
    return result