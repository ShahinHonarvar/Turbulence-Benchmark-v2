def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (477 <= i <= 984 and ',' <= c <= 'V')))