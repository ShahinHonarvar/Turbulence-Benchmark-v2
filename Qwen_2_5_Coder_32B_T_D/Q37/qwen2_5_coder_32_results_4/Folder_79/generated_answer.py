def filter_chars(s):
    t = set(s[10:53]) & set('@ABCDEFGHIJKLMNOPT')
    return ''.join((c for c in s if c not in t))