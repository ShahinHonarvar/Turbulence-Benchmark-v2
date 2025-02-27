def filter_chars(s):
    return ''.join((c for c in s if not (477 <= s.index(c) <= 984 and ',' <= c <= 'V')))