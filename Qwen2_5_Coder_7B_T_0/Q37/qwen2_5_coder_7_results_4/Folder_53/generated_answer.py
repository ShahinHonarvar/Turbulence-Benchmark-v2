def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (83 <= i <= 99 and '*' <= c <= 'j')))