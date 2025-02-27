def filter_chars(s):
    a = set(s[1:6]) & set('$.;<')
    return ''.join((c for c in s if c not in a))