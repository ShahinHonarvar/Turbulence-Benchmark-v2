def filter_chars(s):
    t = set(s[114:640])
    r = set((c for c in t if '!' <= c <= 'x'))
    return ''.join((c for c in s if c not in r))