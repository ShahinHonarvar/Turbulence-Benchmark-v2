def filter_chars(s):
    r = set(s[12:89]) & set('&' + ''.join([chr(i) for i in range(ord('&') + 1, ord('v') + 1)]))
    return ''.join((c for c in s if c not in r))