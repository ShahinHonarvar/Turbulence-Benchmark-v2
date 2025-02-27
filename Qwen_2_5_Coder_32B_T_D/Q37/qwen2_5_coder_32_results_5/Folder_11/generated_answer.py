def filter_chars(s):
    t = set(s[29:98]) & set('-n')
    return ''.join((c for c in s if c not in t))