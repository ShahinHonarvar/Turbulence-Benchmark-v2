def filter_chars(s):
    r = ''.join(sorted(set(s[1:7]) & set('-L')))
    return ''.join((c for c in s if c not in r))