def filter_chars(s):
    t = ''.join(set(s[81:89]) & set('ghijklmnopqrstuvwx'))
    return ''.join((c for c in s if c not in t))