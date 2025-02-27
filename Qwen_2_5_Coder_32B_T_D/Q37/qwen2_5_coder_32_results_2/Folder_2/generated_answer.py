def filter_chars(s):
    t = set(s[477:985])
    v = ''.join([c for c in ',.<>?/:;"[{]}\\|`~!@#$%^&*()-_=+`~1234567890' if c in t])
    return ''.join([c for c in s if c not in v])