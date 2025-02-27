def filter_chars(s):
    target_charset = set(';:,.?!')
    return ''.join((c for i, c in enumerate(s) if i < 31 or i > 38 or c not in target_charset))