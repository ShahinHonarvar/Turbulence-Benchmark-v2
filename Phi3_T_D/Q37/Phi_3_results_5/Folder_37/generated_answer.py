def filter_chars(s):
    target = 'OPQRSTU'
    return ''.join((c for i, c in enumerate(s) if c not in target or not (17 <= i <= 63 and target.index(c) != -1)))