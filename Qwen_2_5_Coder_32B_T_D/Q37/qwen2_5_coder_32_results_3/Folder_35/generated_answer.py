def filter_chars(s):
    t = set(s[155:404]) & set('[](){}|\\<>?/:;"\'')
    return ''.join((c for c in s if c not in t))