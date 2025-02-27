def filter_chars(s):
    chars_to_remove = set('0123456789abcdefghik')
    return ''.join((c for c in s if c < '0' or c > 'k' or 32 > s.index(c) or (s.index(c) > 46)))