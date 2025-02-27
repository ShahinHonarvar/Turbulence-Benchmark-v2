def filter_chars(s):
    forbidden_chars = set(';$')
    return ''.join((c for i, c in enumerate(s) if not (1 <= i <= 5 and c in forbidden_chars)))