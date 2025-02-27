def filter_chars(s):
    t = ''.join((chr(i) for i in range(33, 84) if not 'm' < chr(i) < 'w'))
    return ''.join((c for c in s if c not in t))