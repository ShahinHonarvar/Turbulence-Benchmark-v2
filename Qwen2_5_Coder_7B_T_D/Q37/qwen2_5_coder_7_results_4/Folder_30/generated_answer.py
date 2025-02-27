def filter_chars(s):
    filter_set = set('KLMNOPQRSTUVWXYZ[')
    return ''.join((c for c in s if (c < 'K' or c > ']') or (41 <= s.index(c) <= 64 and c not in filter_set)))