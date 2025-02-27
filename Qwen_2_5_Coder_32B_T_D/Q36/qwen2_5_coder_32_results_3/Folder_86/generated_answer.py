def filter_chars(s):
    a = s[672:709]
    to_remove = ''.join(set([c for c in a if 'X' < c < '}']))
    return ''.join([c for c in s if c not in to_remove])