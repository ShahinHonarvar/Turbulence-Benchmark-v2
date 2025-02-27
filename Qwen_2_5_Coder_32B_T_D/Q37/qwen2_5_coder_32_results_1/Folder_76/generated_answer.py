def filter_chars(s):
    if len(s) < 899:
        return s
    a = s[379:900]
    b = ''.join([c for c in a if c >= 'M' and c <= 'v'])
    return ''.join([c for c in s if c not in b])