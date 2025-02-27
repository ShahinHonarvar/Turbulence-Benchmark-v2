def filter_chars(s):
    return ''.join((c for c in s if not (27 <= index(c, s) <= 85 and '!' <= c <= 'B')))

def index(c, s):
    return s.index(c) if c in s else -1