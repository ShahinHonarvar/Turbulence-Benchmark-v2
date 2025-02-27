def filter_chars(s):
    return ''.join([c for i, c in enumerate(s) if i < 155 or i > 403 or c < '(' or (c > ']')])