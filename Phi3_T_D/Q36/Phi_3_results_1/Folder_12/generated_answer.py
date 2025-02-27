def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not 32 < ord(c) < 84 or (c > 'm' and c < 'w')))