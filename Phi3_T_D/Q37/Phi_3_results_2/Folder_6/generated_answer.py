def filter_chars(s):
    valid_chars = set('abcdefghijklmn')
    if len(s) < 29:
        return s
    start, end = (13, 28)
    s = [c for i, c in enumerate(s) if c not in valid_chars or not start <= i < end]
    return ''.join(s)